# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays CASCADE"
user_table_drop = "DROP TABLE IF EXISTS users CASCADE"
song_table_drop = "DROP TABLE IF EXISTS songs CASCADE"
artist_table_drop = "DROP TABLE IF EXISTS artists CASCADE"
time_table_drop = "DROP TABLE IF EXISTS time CASCADE"

# CREATE TABLES

songplay_table_create = ("""
	CREATE TABLE IF NOT EXISTS songplays(
		songplay_id SERIAL PRIMARY KEY NOT NULL,
		start_time TIME,
		user_id VARCHAR(18) REFERENCES users(user_id),
		level VARCHAR(10),
		song_id VARCHAR(18) REFERENCES songs(song_id),
		artist_id VARCHAR(18) REFERENCES artists(artist_id),
		session_id INT,
		location VARCHAR(255),
		user_agent VARCHAR(255)
	)
""")

user_table_create = ("""
	CREATE TABLE IF NOT EXISTS users(
		user_id VARCHAR(18) PRIMARY KEY  NOT NULL,
		first_name VARCHAR(255) NOT NULL,
		last_name VARCHAR(255) NOT NULL,
		gender CHAR(1) NOT NULL,
		level VARCHAR(10) NOT NULL
	)
""")

song_table_create = ("""
	CREATE TABLE IF NOT EXISTS songs(
		song_id VARCHAR(18) PRIMARY KEY  NOT NULL,
		title VARCHAR(255) NOT NULL,
		duration REAL,
		year SMALLINT,
		artist_id VARCHAR(18) REFERENCES artists(artist_id)
	)
""")

artist_table_create = ("""
	CREATE TABLE IF NOT EXISTS artists(
		artist_id VARCHAR(18) PRIMARY KEY  NOT NULL,
		name VARCHAR(255),
		location VARCHAR(255),
		latitude REAL,
		longitude REAL
	)
""")

time_table_create = ("""
	CREATE TABLE IF NOT EXISTS time(
		start_time TIME PRIMARY KEY,
		hour SMALLINT,
		day SMALLINT,
		week SMALLINT,
		month SMALLINT,
		year SMALLINT,
		weekday SMALLINT
	)
""")

# INSERT RECORDS
#
songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, duration, year, artist_id) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, latitude, longitude) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday) VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS
song_select = ("""
SELECT songs.song_id, songs.artist_id FROM songs, artists WHERE songs.artist_id = artists.artist_id and songs.title = (%s)
""")

# QUERY LISTS
create_table_queries = [user_table_create, artist_table_create, song_table_create, songplay_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
