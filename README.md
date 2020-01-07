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
```
### Fact Table

    *songplays*: records in log data associated with song plays i.e. records with page NextSong
     songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables

    users - users in the app
        user_id, first_name, last_name, gender, level
    songs - songs in music database
        song_id, title, artist_id, year, duration
    artists - artists in music database
        artist_id, name, location, latitude, longitude
    time - timestamps of records in songplays broken down into specific units
        start_time, hour, day, week, month, year, weekday
```
### Code files

    *create_tables.py*
    *etl.py*



## Run Data pipeline
```
python etl.py 
```

