# Bigdata modeling
Data Engineering Project: Big Data modeling using postgreSQL




## prerequisite

* PostgreSQL
* Python 3.6 or higher


## Dependencies
```
pip install -r requirements.txt
```

## DB Setup
```
export DB_USER = <PostgreSQL DB user>
export DB_PASS = <PostgreSQL DB password>
export DB_SERVER = <PostgreSQL DB server IP>. It defaults to 127.0.0.1

python create_tables.py 

```
## DB Schema

### Fact Table

    **sonboldbolfgplays** : records in log data associated with song plays i.e. records with page NextSong

### Dimension Tables

    **users** - users in the app
    **songs** - songs in music database
    **artists** - artists in music database
    **time** - timestamps of records in songplays broken down into specific units

### Code files

    **create_tables.py** - to create Database and tables
    **etl.py** - to insert/update data 


## Run Data pipeline
```
python etl.py 
```

