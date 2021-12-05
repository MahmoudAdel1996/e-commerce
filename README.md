# e-commerce

postgres version `PostgreSQL 10.7, compiled by Visual C++ build 1800, 64-bit`

## install DataBase for linux
using postgres after clone the project do these things to restore database in your computer.  
```sql	
CREATE DATABASE ecommerce;
```  

```bash
$ pg_restore --dbname=ecommerce --verbose backupDB.sql
```
## Required Packages

|Package            |Version
|------------------ |-------
|asgiref            |3.3.4
|click              |8.0.1
|colorama           |0.4.4
|Django             |3.2.3
|importlib-metadata |4.3.1
|joblib             |1.0.1
|nltk               |3.6.2
|numpy              |1.20.3
|pandas             |1.1.5
|Pillow             |8.2.0
|pip                |21.1.2
|psycopg2           |2.8.6
|python-dateutil    |2.8.1
|pytz               |2021.1
|rake-nltk          |1.0.4
|regex              |2021.4.4
|scikit-learn       |0.24.2
|scipy              ||1.6.3
|setuptools         |57.0.0
|six                |1.16.0
|sklearn            |0.0
|sqlparse           |0.4.1
|threadpoolctl      |2.1.0
|tqdm               |4.61.0
|typing-extensions  |3.10.0.0
|zipp               |3.4.1
