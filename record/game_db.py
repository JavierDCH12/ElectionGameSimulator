import mysql.connector
from mysql.connector import Error
import datetime
from dotenv import load_dotenv
import os


load_dotenv()
db_host=os.getenv('DB_HOST')
db_user=os.getenv('DB_USER')
db_passwd=os.getenv('DB_PASSWORD')



#CONNECTION TO MYSQL
def create_connect_db():
    try:
        connection=mysql.connector.connect(
            host=db_host,
            user=db_user,
            passwd=db_passwd,
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
def add_event_db(connection, session_id, event, impact):
    cursor = connection.cursor()
    query = """
    INSERT INTO events (session_id, event, impact)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (session_id, event, impact))
    connection.commit()
    
#FUNCTION TO ADD ACTION
def add_action_db(connection, session_id, action):
    cursor = connection.cursor()
    # Extract costs from the action object
    cost_financial = action.cost.get('financial', 0)
    cost_influence = action.cost.get('influence', 0)
    cost_internal = action.cost.get('internal', 0)
    
    query = """
    INSERT INTO actions (session_id, politician_name, action_name, cost_financial, cost_influence, cost_internal, benefit)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (session_id, action.politician_name, action.name, cost_financial, cost_influence, cost_internal, action.benefit))
    connection.commit()
