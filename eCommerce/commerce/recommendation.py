import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds
from .models import Invoices

# Sales = pd.read_excel('train.xlsx')
# Products = pd.read_excel('Products.xlsx')
Sales = Invoices.objects.values('customer_id', 'product_id', 'quantity')
Sales = pd.DataFrame(list(Sales.values()))
Sales['Total_Quantity'] = Sales.groupby(['customer_id', 'product_id'])['quantity'].transform('sum')
Sales = Sales.drop_duplicates(subset=['customer_id', 'product_id'], keep='first')
Sales = Sales.drop('quantity', axis=1)


def recommender_2():
    # top sales products recommendation
    sales_count = Sales.groupby(['product_id'], as_index=False, sort=False).sum()[['product_id', 'Total_Quantity']]
    sales_count = sales_count.sort_values('Total_Quantity', ascending=False)
    sales_count = sales_count.drop('Total_Quantity', axis=1)
    return list(sales_count['product_id'])


def recommender(user_id, n=10):

    if not user_id:
        user_id = 1
    reshape_purchases = Sales.pivot(index='customer_id', columns='product_id', values='Total_Quantity')
    users_mean = np.array(reshape_purchases.mean(axis=1))
    r_demeaned = reshape_purchases.sub(reshape_purchases.mean(axis=1), axis=0)
    r_demeaned = r_demeaned.fillna(0).values

    u, sigma, vt = svds(r_demeaned, k=50)
    sigma = np.diag(sigma)

    all_user_predicted_ratings = np.dot(np.dot(u, sigma), vt) + users_mean.reshape(-1, 1)
    preds_df = pd.DataFrame(all_user_predicted_ratings, columns=reshape_purchases.columns)

    recommendation = preds_df.iloc[user_id - 1].sort_values(ascending=False)
    recommendation = recommendation[:n]
    recommendation = recommendation.to_frame()

    return list(recommendation.T.columns.values)
