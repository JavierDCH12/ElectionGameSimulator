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
    
    #Creation of the politician with all its atributes
    print("Let's create your desired candidate: ")
    name=ask_name()
    age=ask_age()
    gender=ask_gender()
    
    party=random.choice(CONSTANTS.PARTIES)
    prefecture=random.choice(CONSTANTS.PREFECTURES)
    
    return Politician(name, age, gender, party, prefecture)
        


def create_ai_politician():
    age = random.randint(25, 100) 
    gender = random.choice(["Male", "Female"])
    
    if gender == "Male":
        name = random.choice(CONSTANTS.MALE_NAMES)
    elif gender=="Female":
        name= random.choice(CONSTANTS.FEMALE_NAMES)
    
    party=random.choice(CONSTANTS.PARTIES)
    prefecture=random.choice(CONSTANTS.PREFECTURES)
    
    return Politician(name, age, gender, party, prefecture)



def age_bonus(politician: Politician) -> int:
    score = 0
    if politician.age >= 80:
        score = 5
    elif 60 <= politician.age < 80:
        score = 10
    elif 40 <= politician.age < 60:
        score = 15
    elif 25 <= politician.age < 40:
        score = 5
    return score  


def set_initial_score(politician : Politician):
    score = 0
    
    score+=CONSTANTS.PARTY_POPULARITY.get(politician.party.name, 0) #ADD PARTY POINTS
    
    score +=CONSTANTS.PREFECTURE_BONUS.get(politician.prefecture.name, 0) #ADD PREFECTURE POINTS
    
    score +=age_bonus(politician)

    return score


def week_simulation(politician, is_user=True): #With is_user cwe control the message tailored for the ai of your player
    event, impact = random.choice(CONSTANTS.EVENTS)
    if is_user:
        print(f"Something happened this week: {event} with an impact of {impact} points in your score")
    if not is_user:
        print(f"Something happened this week: {event} with an impact of {impact} points in the score of your adversary")
        
    return impact

def simulate_election(politician, score, is_user=True):
    impact = week_simulation(politician, is_user)
    score += impact
    print(f"Score after this week: {score}")
    return score