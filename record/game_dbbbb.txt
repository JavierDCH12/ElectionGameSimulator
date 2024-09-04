import sqlite3
import re
import pandas as pd
import os

log_path = "logs/pols.log"

connection = sqlite3.connect("record/game.db")
cursor = connection.cursor()

cursor.execute('''DROP TABLE Politicians''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Politicians (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    experience TEXT,
    party TEXT,
    prefecture TEXT,
    log_time TEXT
)
''')

# Función para extraer datos del log y guardar en la base de datos
def extract_pol_data(log_path):
    if not os.path.exists(log_path):
        print(f"Log file {log_path} does not exist.")
        return
    
    with open(log_path, 'r') as file:
        for line in file:
            # Buscar coincidencias utilizando regex
            match = re.search(
                r"INFO - Name: (?P<name>.+?) \| Age: (?P<age>\d+) \| Gender: (?P<gender>Male|Female)(?: \| Experience: (?P<experience>Incumbent|New Candidate))? \| Political Party: (?P<party>.+?) \| Prefecture: (?P<prefecture>.+)", 
                line
            )
            if match:
                # Extraer los datos capturados por el regex
                name = match.group('name')
                age = match.group('age')
                gender = match.group('gender')
                experience = match.group('experience') if match.group('experience') else 'Not Provided'
                party = match.group('party')
                prefecture = match.group('prefecture')
                
                # Extraer la marca de tiempo del log
                log_time = line.split(" - ")[0]
                
                # Insertar los datos en la base de datos
                cursor.execute('''
                INSERT INTO Politicians (name, age, gender, experience, party, prefecture, log_time)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (name, int(age), gender, experience, party, prefecture, log_time))
                print(f"Inserted data into database: Name={name}, Age={age}, Gender={gender}, Experience={experience}, Party={party}, Prefecture={prefecture}, Log Time={log_time}")

# Ejecutar la función para extraer los datos del log
extract_pol_data(log_path)
connection.commit()

# Cargar los datos en un DataFrame de pandas
data = pd.read_sql_query('SELECT * FROM Politicians', connection)
print(data)

cursor.close()
connection.close()
