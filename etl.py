import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Process json song file and update respective DB tables.

    Parameters:
    cur (Object): Database cursor
    filepath (str): json file path
    """
    # open song file
    ser = pd.read_json(filepath, typ='series')
    df = ser.to_frame('count')

    # insert artist record
    artist_data = (df.loc['artist_id', 'count'], df.loc['artist_name', 'count'], df.loc['artist_location', 'count'], df.loc['artist_latitude', 'count'], df.loc['artist_longitude', 'count'])
    cur.execute(artist_table_insert, artist_data)

    # insert song record
    song_data = (df.loc['song_id', 'count'], df.loc['title', 'count'], df.loc['duration', 'count'], df.loc['year', 'count'], df.loc['artist_id', 'count'])
    cur.execute(song_table_insert, song_data)

def process_log_file(cur, filepath):
    """
    Process json log file and update respective DB tables.

    Parameters:
    cur (Object): Database cursor
    filepath (str): json file path
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong actionpytpon
    is_next_song = df['page'] == 'NextSong'
    df = df[is_next_song]

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')

    # insert time data records
    time_df = pd.DataFrame(data={'start_time': t.dt.time,
                                'hour': t.dt.hour,
                                'day': t.dt.day,
                                'week': t.dt.week,
                                'month': t.dt.month,
                                'year': t.dt.year,
                                'weekday': t.dt.weekday
                                })

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)
    df['start_time'] = pd.to_datetime(df['ts'], unit='ms')
    # insert songplay records
    for index, row in df.iterrows():
        # get songid and artistid from song tables
        cur.execute(song_select, (row.song,))
        results = cur.fetchone()
        songid, artistid = results if results else (None, None)

        # insert songplay record
        songplay_data = (row.start_time, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)

def process_data(cur, conn, filepath, func):
    """
    reads json data files and process them

    Parameters:
    cur (Object): Database cursor
    conn (Object): Database connection
    filepath (str): directory path that contains all log files.

    """

    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    db_server = os.getenv("DB_SERVER", "127.0.0.1")
    db_user = os.getenv("DB_USER", None)
    db_pass = os.getenv("DB_PASSORD", None)
    if db_pass:
        conn = psycopg2.connect("host={} dbname=sparkifydb user={}, password={}".format(db_server, db_user, db_pass))
    else:
        conn = psycopg2.connect("host={} dbname=sparkifydb user={}".format(db_server, db_user))
    cur = conn.cursor()

    # Song files
    try:
        process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    except Exception as e:
        print(e)

    # Log files
    try:
        process_data(cur, conn, filepath='data/log_data', func=process_log_file)
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    main()