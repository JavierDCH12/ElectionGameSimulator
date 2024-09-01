import sqlite3
import re

#CREATE DATABASE
connection = sqlite3.connect("record/game.db")
cursor = connection.cursor()

#CREATE TABLE
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


def extract_pol_data(log_path):
    with open(log_path, 'r') as file:
        for line in file:
            match = re.search(r"INFO - Name: (?P<name>.+?) \| Age: (?P<age>\d+|None) \| Gender: (?P<gender>Male|Female) \| Experience: (?P<experience>Incumbent|New candidate) \| Political Party: (?P<party>.+?) \| Prefecture: (?P<prefecture>.+)", line)
            if match: 
                name=match.group('name')
                age=match.group('age')
                gender=match.group('gender')
                experience=match.group('experience')
                party=match.group('party')
                prefecture=match.group('prefecture')
                
                
                log_time = line.split(" - ")[0]
                
                cursor.execute('''
                INSERT INTO Politicians (name, age, gender, experience, party, prefecture, log_time)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (name, age, gender, experience, party, prefecture, log_time))
                
extract_pol_data("logs\pols.log")   

connection.commit()
#cursor.close()
cursor.execute("SELECT * FROM Politicians")


        