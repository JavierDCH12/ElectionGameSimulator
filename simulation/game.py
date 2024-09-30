import logging
from src.politician import Politician
from src.cons import CONSTANTS
from src.cons import STRINGS
from src.cons import INTS


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
    return input(f"{STRINGS.INPUT_NAME}").capitalize()

def ask_age() -> int:
    while True:
        try:
            age = int(input(f"{STRINGS.INPUT_AGE}"))
            if INTS.BOTTOM_AGE <= age <= INTS.TOP_AGE:
                return age
            else:
                print(f"{STRINGS.AGE_ERROR_1}")
                logger_error.error(f"\nInvalid input for age: {age}\n", exc_info=True)
        except ValueError as e:
            print(f"{STRINGS.AGE_ERROR_2}")
            logger_error.error(f"\nInvalid input for age: {e}\n", exc_info=True)


def ask_gender() -> str:
    while True:
        gender = input(f"{STRINGS.INPUT_GENDER}").capitalize()
        if gender in ["Male", "Female"]:
            return gender
        else:
            logger_error.error(f"\nInvalid gender: {gender}\n", exc_info=True)
            print(f"{STRINGS.GENDER_ERROR}")

def create_politician():
    print(f"{STRINGS.CANDIDATE_CREATION}")
    name = ask_name()
    age = ask_age()
    gender = ask_gender()
    
    experience = random.choice(list(CONSTANTS.EXPERIENCE_LEVEL_MODIFIER.keys()))
    party = random.choice(CONSTANTS.PARTIES)
    prefecture = random.choice(CONSTANTS.PREFECTURES)
    
    politician= Politician(name, age, gender, experience, party, prefecture)
    return politician

def create_ai_politician():
    age = random.randint(INTS.BOTTOM_AGE, INTS.TOP_AGE)
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
    return random.uniform(INTS.BOTTOM_SCORE_MODIFIER, INTS.TOP_SCORE_MODIFIER)


def generate_random_event() -> tuple:
    """Generate a random event and its base impact."""
    if random.random() < INTS.SPECIAL_EVENTS:
        event = random.choice(CONSTANTS.SPECIAL_EVENTS)
    else:
        event = random.choice(CONSTANTS.EVENTS)
    return event


def generate_impact(politician, is_player=False, event=None) -> int:
    event = generate_random_event()
    base_impact=event.impact
    
    modifier = random_score_modifier()
    final_impact = round(base_impact * modifier)
    """if event.impact > 0:
        impact = max(0, final_impact)  # Ensure positive impact stays positive or zero
    else:
        impact = min(0, impact)  # Ensure negative impact stays negative or zero
    """
    
    
    print(f"{politician.name}\n: {STRINGS.EVENT}'{event}' {STRINGS.MODIFIED_IMPACT} {final_impact} {STRINGS.POINTS}.")
    
    log_event(politician.name, event.name, event.impact, politician.points + final_impact)

    
    return final_impact

def generate_score(politician, score, is_player=True, strategy=None) -> int:
    impact = generate_impact(politician, is_player)
    
    if strategy:
        impact = apply_strategy_modifiers(strategy, impact)
    
    score += impact
    score = max(0, score)
        
    print(f"{STRINGS.WEEKLY_SCORE}{score}\n")
    return score


def final_score_msg(player_score, ai_score):
    if player_score > ai_score:
        print(f"{STRINGS.PLAYER_WIN}")
        print("""
  ____    _    _   _ _____   _    ___  
 | __ )  / \  | \ | |__  /  / \  |_ _| 
 |  _ \ / _ \ |  \| | / /  / _ \  | |  
 | |_) / ___ \| |\  |/ /_ / ___ \ | |  
 |____/_/   \_\_| \_/____/_/   \_\___| """)
    elif ai_score > player_score:
        print(f"{STRINGS.AI_WIN}")
        print("""
  / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
 | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
 | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
  \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
        """)














