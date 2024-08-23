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


def random_score_modifier():
    return random.uniform(0.8, 1.2)

def set_initial_score(politician : Politician):
    score = 0
    
    score+=CONSTANTS.PARTY_POPULARITY.get(politician.party.name, 0) #ADD PARTY POINTS
    
    score +=CONSTANTS.PREFECTURE_BONUS.get(politician.prefecture.name, 0) #ADD PREFECTURE POINTS
    
    score +=age_bonus(politician)

    return score


def week_simulation(politician, is_user=False):
    
    if random.random() < 0.2:  
        event, base_impact = random.choice(CONSTANTS.SPECIAL_EVENTS)
    else:
        event, base_impact = random.choice(CONSTANTS.EVENTS)
    
    modifier = random_score_modifier() 
    impact = round(base_impact * modifier)
    
    # Asegurar que el puntaje no sea negativo
    impact = max(0, impact) if base_impact > 0 else min(0, impact)
    
    if is_user:
        print(f"Your candidate experienced: {event}, resulting in an impact of {impact} points.")
        
    else:
        
        print(f"The AI's candidate experienced: {event}, resulting in an impact of {impact} points.")
    
    return impact

def simulate_election(politician, score, is_user=True):
    impact = week_simulation(politician, is_user)
    score += impact
    if score<0:
        score=0
    print(f"Score after this week: {score}")
    return score
    

def final_score_msg(player_score, ai_score):
    if player_score > ai_score:
        print("You have been elected President of Japan!")
        print("""
  ____    _    _   _ _____   _    ___  
 | __ )  / \  | \ | |__  /  / \  |_ _| 
 |  _ \ / _ \ |  \| | / /  / _ \  | |  
 | |_) / ___ \| |\  |/ /_ / ___ \ | |  
 |____/_/   \_\_| \_/____/_/   \_\___| """)
    elif ai_score > player_score:
        print("The AI candidate has won the election...")
        print("""
  / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
 | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
 | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
  \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
        """)