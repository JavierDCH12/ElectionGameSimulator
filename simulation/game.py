from src.politician import Politician
from src import CONSTANTS

import random

def ask_name() -> str:
    return input("Enter the politician's name: ").capitalize()

def ask_age() -> int:
    while True:
        try:
            age = int(input("Enter the politician's age: "))
            if 25 <= age <= 100:
                return age
            else:
                print("Age must be between 25 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")



def ask_gender() -> str:
    while True:
        gender = input("Enter the politician's gender (Male/Female): ").capitalize()
        
        if gender in ["Male", "Female"]:
            return gender
        else:
            print("Gender must be 'Male' or 'Female'. Please try again.")




def create_politician():
    name=ask_name()
    age=ask_age()
    gender=ask_gender()
    
    party=random.choice(CONSTANTS.PARTIES)
    prefecture=random.choice(CONSTANTS.PREFECTURES)
    
    return Politician(name, age, gender, party, prefecture)
        
    
    