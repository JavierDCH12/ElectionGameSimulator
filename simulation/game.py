from src.politician import Politician
from src import CONSTANTS

import random

def ask_name() -> str:
    return input("Enter the politician's name: ")

def ask_age() -> int:
    age = int(input("Enter the politician's age: "))
    if age < 25 or age > 100:
        raise ValueError("Age can't be lower than 25 or higher than 100")
    return age

def ask_gender() -> str:
    gender = input("Enter the politician's gender (Male/Female): ").capitalize()
    if gender not in ["Male", "Female"]:
        raise ValueError("Gender must be 'Male' or 'Female'")
    return gender




def create_politician():
    name=ask_name()
    age=ask_age()
    gender=ask_gender()
    
    party=random.choice(CONSTANTS.PARTIES)
    prefecture=random.choice(CONSTANTS.PREFECTURES)
    
    return Politician(name, age, gender, party, prefecture)
        
    
    