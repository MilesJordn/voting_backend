import os  
import sqlite3

PATH_TO_DB = os.path.join(
    os.path.dirname(__file__),
    "db.sqlite"
)

if os.path.exists(PATH_TO_DB):
    os.unlink(PATH_TO_DB) 


create_session_table_query = "CREATE TABLE session(id_session INTEGER PRIMARY KEY AUTOINCREMENT, session_name TEXT, session_date DATE, winner TEXT)";


create_candidate_table_query = "CREATE TABLE candidate (name TEXT, candidate_id INTEGER PRIMARY KEY AUTOINCREMENT, post TEXT, candidate_class TEXT,  id_session INTEGER, FOREIGN KEY(id_session) REFERENCES session(id_session))";


create_votes_table_query = "CREATE TABLE votes (id_votes INTEGER PRIMARY KEY AUTOINCREMENT, participant_id INTEGER, candidate_id INTEGER, FOREIGN KEY(candidate_id) REFERENCES candidate(candidate_id))";


with sqlite3.connect(PATH_TO_DB) as connection:
    cursor = connection.cursor()

    for query in [create_session_table_query,create_candidate_table_query, create_votes_table_query]:
        cursor.execute(query)           