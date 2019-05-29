# e-commerce

## DataBase
using postgres after clone the project do this things to restore database in your computer.  
```sql	
CREATE DATABASE ecommerce;
```  

```bash
$ pg_restore --dbname=ecommerce --verbose backupDB.sql
```
## Required Pakages

|Package    |Version
|---------- |-------
|Django     |2.2.1
|Pillow     |6.0.0
|psycopg2   |2.8.2
