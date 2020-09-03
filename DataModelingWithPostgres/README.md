
# Proyect: Data
## Author: Jesús Velayos Herrero

## Objetive: 
Sparkify wants the creation of a Postgres database with tables designed to optimize queries on song play analysis. This project consist in the creation of the database's schema and ETL pipeline.

The purpose of this database in the context of Sparkify is to ***optimize queries on song play analysis***. 


Using the song and log datasets I created a star schema optimized for queries on song play analysis. This includes the following tables:

### Fact Table
**SONGPLAYS** - records in log data associated with song plays i.e. records with page NextSong. Rows:

* songplay_id 
* start_time
* user_id
* level
* song_id
* artist_id
* session_id 
* location
* user_agent

### Dimension Tables
Table **USERS**: Table with the info about the users in the app
* user_id
* first_name
* last_name
* gender
* level

**SONGS** (songs in music database)
* song_id
* title
* artist_id
* year
* duration

**ARTISTS** (artists in music database)
* artist_id
* name
* location
* latitude
* longitude
**TIME** (timestamps of records in songplays broken down into specific units)
* start_time
* hour
* day
* week
* month
* year
* weekday

## Instructions:
You need to install previously Postgres and Python3, after that:

### Creation of the database and the tables:
+ Directly in a terminal window execute: python3 create_tables.py

### Insertions of information in the tables:
+ Directly in a terminal window execute: python3 etl.py




## State and justify your database schema design and ETL pipeline.
The star squema used for solve this project is a good solution because the simpler logic of this squema allows for easier and faster queries, easier reporting, and simple aggregations faster because fewer tables are involved.

### Example queries and results for song play analysis.

Number of songs played in weekends days grouped by day:

`SELECT t.weekday
     , COUNT( * ) AS n_plays 
FROM songplays s
    ,time t 
WHERE s.start_time = t.start_time 
      AND weekday in  (5,6) 
GROUP BY t.weekday ORDER BY n_plays DESC;`

| weekday | n_plays |
|:-:      |:-:      |
|     5   |   632   |
|     6   |   396   |


Number of artists with names starting with 'A':
`SELECT count(*) AS num_artist_a 
FROM artists 
WHERE name like 'A%';`

| num_artists_a |
|:-:            |
|       3       |
