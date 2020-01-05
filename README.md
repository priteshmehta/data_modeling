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

## Run Data pipeline
```
python etl.py 
```
