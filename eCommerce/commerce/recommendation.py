import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds
from .models import Invoices, Products
from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


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
    else:
        user_id = user_id.id
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


def products_recommender(products, product_id=1):
    df = pd.DataFrame(list(products.values()))

    # initializing the new column
    df['Key_words'] = ""
    x = []
    for index, row in df.iterrows():
        product_name = row['name']
        # instantiating Rake, by default is uses english stopwords from NLTK
        r = Rake()

        # extracting the words by passing the text
        r.extract_keywords_from_text(product_name)

        # getting the dictionary whith key words and their scores
        key_words_dict_scores = r.get_word_degrees()

        # assigning the key words to the new column
        row['Key_words'] = list(key_words_dict_scores.keys())
        str1 = ' '.join(row['Key_words'])
        x.append(str1)

    df['Key_words'] = x

    count = TfidfVectorizer()
    count_matrix = count.fit_transform(df['Key_words'])
    # generating the cosine similarity matrix
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # function that takes in movie title as input and returns the top 10 recommended movies

    recommended_movies = []

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[product_id]).sort_values(ascending=False)

    # getting the indexes of the 10 most similar movies
    top_10_indexes = list(score_series.iloc[1:11].index)

    # populating the list with the titles of the best 10 matching movies
    for i in top_10_indexes:
        recommended_movies.append(list(df.index)[i]+1)
    print(recommended_movies)
    return recommended_movies
