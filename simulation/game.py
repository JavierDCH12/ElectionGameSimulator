import logging
from src.politician import Politician
from src import CONSTANTS
import random
from simulation.user_decisions import apply_strategy_modifiers
from simulation.log_actions import log_event

logger_error = logging.getLogger(__name__)
logger_error.setLevel(logging.ERROR)  
file_handler = logging.FileHandler('logs/errors.log')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger_error.addHandler(file_handler)



############################################################################################
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
                logger_error.error(f"\nInvalid input for age: {age}\n", exc_info=True)
        except ValueError as e:
            print("Invalid input. Please enter a valid integer for age.")
            logger_error.error(f"\nInvalid input for age: {e}\n", exc_info=True)


def ask_gender() -> str:
    while True:
        gender = input("Enter the politician's gender (Male/Female): ").capitalize()
        if gender in ["Male", "Female"]:
            return gender
        else:
            logger_error.error(f"\nInvalid gender: {gender}\n", exc_info=True)
            print("Gender must be 'Male' or 'Female'. Please try again.")

def create_politician():
    print("Let's create your desired candidate: ")
    name = ask_name()
    age = ask_age()
    gender = ask_gender()
    
    experience = random.choice(list(CONSTANTS.EXPERIENCE_LEVEL_MODIFIER.keys()))
    party = random.choice(CONSTANTS.PARTIES)
    prefecture = random.choice(CONSTANTS.PREFECTURES)
    
    politician= Politician(name, age, gender, experience, party, prefecture)
    return politician

def create_ai_politician():
    age = random.randint(25, 100)
    gender = random.choice(["Male", "Female"])
    
    name = random.choice(CONSTANTS.MALE_NAMES) if gender == "Male" else random.choice(CONSTANTS.FEMALE_NAMES)
    
    experience = random.choice(list(CONSTANTS.EXPERIENCE_LEVEL_MODIFIER.keys()))
    party = random.choice(CONSTANTS.PARTIES)
    prefecture = random.choice(CONSTANTS.PREFECTURES)
    
    politician= Politician(name, age, gender, experience, party, prefecture)
    return politician



def age_bonus(politician: Politician) -> int:
    if politician.age >= 80:
        return CONSTANTS.AGE_BONUS["80+"]
    elif 60 <= politician.age < 80:
        return CONSTANTS.AGE_BONUS["60-80"]
    elif 40 <= politician.age < 60:
        return CONSTANTS.AGE_BONUS["40-60"]
    elif 25 <= politician.age < 40:
        return CONSTANTS.AGE_BONUS["25-40"]
    return 0


def experience_bonus(politician: Politician) -> float:
    return CONSTANTS.EXPERIENCE_LEVEL_MODIFIER.get(politician.experience, 1.0)

def set_initial_score(politician: Politician) -> int:
    # Calculate base score from various factors
    score = 0
    score += CONSTANTS.PARTY_POPULARITY_BONUS.get(politician.party.name, 0)  # ADD PARTY BONUS
    score += CONSTANTS.PREFECTURE_BONUS.get(politician.prefecture.name, 0)  # ADD PREFECTURE POINTS
    score += age_bonus(politician)  # ADD AGE BONUS

    # Apply experience modifier after calculating the base score
    experience_modifier = experience_bonus(politician)
    score = round((score) + score * experience_modifier)
    
    return score

def random_score_modifier() -> float:
    return random.uniform(0.8, 1.2)


def generate_random_event() -> tuple:
    """Generate a random event and its base impact."""
    if random.random() < 0.2:
        event, base_impact = random.choice(CONSTANTS.SPECIAL_EVENTS)
    else:
        event, base_impact = random.choice(CONSTANTS.EVENTS)
    return event, base_impact


def generate_impact(politician, is_player=False, event=None, base_impact=None) -> int:
    event, base_impact = generate_random_event()
    
    modifier = random_score_modifier()
    impact = round(base_impact * modifier)
    
    if base_impact > 0:
        impact = max(0, impact)  # Ensure positive impact stays positive or zero
    else:
        impact = min(0, impact)  # Ensure negative impact stays negative or zero
    
    print(f"{politician.name} experienced: '{event}', with an impact of {impact} points.")
    
    log_event(politician.name, event, impact, politician.points + impact)

    
    return impact

def generate_score(politician, score, is_player=True, strategy=None) -> int:
    impact = generate_impact(politician, is_player)
    
    if strategy:
        impact = apply_strategy_modifiers(strategy, impact)
    
    score += impact
    score = max(0, score)
        
    print(f"Score after this week: {score}\n")
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














