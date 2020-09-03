# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artist"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays (songplay_id serial primary key not null, \
                                                  start_time timestamp not null, \
                                                  user_id numeric not null, \
                                                  level varchar, \
                                                  song_id varchar not null, \
                                                  artist_id varchar not null, \
                                                  session_id varchar not null, \
                                                  location varchar, \
                                                  user_agent varchar);""")

user_table_create = ("""create table if not exists users (user_id integer primary key, \
                                          first_name varchar, \
                                          last_name varchar, \
                                          gender varchar, \
                                          level varchar);""")

song_table_create = ("create table if not exists songs (song_id varchar primary key, \
                                          title varchar, \
                                          artist_id varchar, \
                                          year integer, \
                                          duration decimal);""")

artist_table_create = ("""create table if not exists artists (artist_id varchar primary key, \
                                              name varchar, \
                                              location varchar, \
                                              latitude decimal, \
                                              longitude decimal);""")

time_table_create = ("""create table if not exists time (start_time  timestamp not null, \
                                         hour int, \
                                         day int, \
                                         week int, \
                                         month int, \
                                         year int, \
                                         weekday int);""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""");

user_table_insert = ("""insert into users values (%s,%s,%s,%s,%s) on conflict (user_id) do nothing""")

song_table_insert = ("""insert into songs values (%s,%s,%s,%s,%s) on conflict (song_id) do nothing;""")

artist_table_insert = ("""insert into artists values (%s,%s,%s,%s,%s) on conflict (artist_id) do nothing;""")

time_table_insert = ("""insert into time values (%s,%s,%s,%s,%s,%s,%s)""")

#FIND SONGS
song_select = ("""SELECT s.song_id, a.artist_id \
                    FROM songs AS s \
                    LEFT JOIN artists AS a \
                    ON a.artist_id = s.artist_id \
                    WHERE   s.title = (%s) AND \
                            a.name = (%s) AND \
                            s.duration = (%s);""")
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


    