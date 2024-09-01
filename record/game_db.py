import mysql.connector
from mysql.connector import Error
import datetime

#CONNECTION TO MYSQL
def create_connect_db():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="election_game_simulator"
        )
        if connection.is_connected():
            print("Successful connection to MYSQL")
            return connection
        
    except Error as e:
        print(f"Can't connect to MYSQL: {e}")
        return None


#FUNCTION TO RECORD GAME SESSION
def add_game_session_db(connection, session_id, player, ai, start_time):
    cursor = connection.cursor()
    query = """
    INSERT INTO game_sessions (session_id, player_name, ai_name, start_time)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (session_id, player.name, ai.name, start_time))
    connection.commit()

#FUNCTION TO RECORD POLITICIAN
def add_politician_db(connection, politician, session_id):
    cursor = connection.cursor()
    query = """
    INSERT INTO politicians (name, party, age, experience, financial_resources, influence_resources, internal_resources, points, session_id, created_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    # Extraer atributos del objeto politician
    cursor.execute(query, (
        politician.name, politician.party.name, politician.age, politician.experience,
        politician.resources['financial'], politician.resources['influence'], politician.resources['internal'],
        politician.points, session_id, datetime.now()
    ))
    connection.commit()

#FUNCTION TO ADD EVENT
def add_event_db(connection, session_id, event_description, impact):
    cursor = connection.cursor()
    query = """
    INSERT INTO events (session_id, event_description, impact)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (session_id, event_description, impact))
    connection.commit()
    
#FUNCTION TO ADD ACTION
def add_action_db(connection, session_id, politician_name, action_name, result):
    cursor = connection.cursor()
    query = """
    INSERT INTO actions (session_id, politician_name, action_name, result)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (session_id, politician_name, action_name, result))
    connection.commit()

