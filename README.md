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

|Package         |Version
|--------------- |-------
|Django          |2.2.1
|numpy           |1.16.4
|pandas          |0.24.2
|Pillow          |6.0.0
|psycopg2        |2.8.2
|scipy           |1.3.0
|rake_nltk       |.....
|sklearn         |.....
|rake-nltk       |1.0.4
