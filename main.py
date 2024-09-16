import logging
import time
import os
import random
from simulation.game import create_politician, create_ai_politician, set_initial_score, final_score_msg
from simulation.resources import set_initial_financial_resources, set_initial_internal_resources, set_initial_personal_resources
from simulation.user_decisions import set_strategy, show_actions
import src.cons.CONSTANTS as CONSTANTS
import src.cons.STRINGS as STRINGS

from simulation.ai_simulation import run_ai_simulation
from simulation.player_simulation import run_player_simulation
from simulation.log_actions import log_strategy
from simulation.menu import intro_menu_option




logger_pols = logging.getLogger(__name__)
logger_pols.setLevel(logging.INFO)  
file_handler = logging.FileHandler('logs/pols.log')
file_handler.setLevel(logging.INFO)  
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger_pols.addHandler(file_handler)

logger_simulation = logging.getLogger(__name__)
logger_simulation.setLevel(logging.INFO)  
file_handler = logging.FileHandler('logs/simulation.log')
file_handler.setLevel(logging.INFO)  
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger_simulation.addHandler(file_handler)




###############################################################
def print_start_message():
    

    # Clear the screen (works on most systems)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the start message in a styled format
    print("""
  _____ _           _   _              ____                      ____  _ 
| ____| | ___  ___| |_(_) ___  _ __  / ___| __ _ _ __ ___   ___/ ___|(_)
|  _| | |/ _ \/ __| __| |/ _ \| '_ \| |  _ / _` | '_ ` _ \ / _ \___ \| |
| |___| |  __/ (__| |_| | (_) | | | | |_| | (_| | | | | | |  __/___) | |
|_____|_|\___|\___|\__|_|\___/|_| |_|\____|\__,_|_| |_| |_|\___|____/|_|
 _ __ ___  _   _| | __ _| |_ ___  _ __                                  
| '_ ` _ \| | | | |/ _` | __/ _ \| '__|                                 
| | | | | | |_| | | (_| | || (_) | |                                    
|_| |_| |_|\__,_|_|\__,_|\__\___/|_|                                                 
""")

    
    print("Welcome to Election Game Simulator!")
    time.sleep(2)  # Pause for 2 seconds to let the user read the message


def display_initial_candidate_resources(player, ai):
    
    print("\nYour candidate:")
    print(f"{player}")
    print(f"Initial Score: {player.points}")
    print(f"Financial Resources: {player.resources.financial_resources} | "
          f"Influence Resources: {player.resources.influence_resources} | "
          f"Internal Resources: {player.resources.internal_resources}")
    print(f"Total Resources: {player.resources.total_resources()}")  # Total Resources
    time.sleep(2)
    
    print("\nA.I Candidate:")
    print(f"{ai}")
    print(f"Initial Score: {ai.points}")
    print(f"Financial Resources: {ai.resources.financial_resources} | "
          f"Influence Resources: {ai.resources.influence_resources} | "
          f"Internal Resources: {ai.resources.internal_resources}")
    print(f"Total Resources: {ai.resources.total_resources()}")  # Total Resources



def initialize_candidate_resources(candidate):
    """Initialize the candidate's points and resources."""
    candidate.points = set_initial_score(candidate)
    candidate.resources.financial_resources = set_initial_financial_resources(candidate)
    candidate.resources.influence_resources = set_initial_personal_resources(candidate)
    candidate.resources.internal_resources = set_initial_internal_resources(candidate)


def run_game():
    logger_simulation.info(f"{STRINGS.GAME_STARTS}\n")
    print_start_message()
    player = create_politician()
    logger_pols.info(player)
    time.sleep(3)
    ai = create_ai_politician()
    logger_pols.info(ai)
    time.sleep(2)
    
    #Set initial scores and resources
    player.points = set_initial_score(player)
    ai.points = set_initial_score(ai)
    initialize_candidate_resources(player)
    initialize_candidate_resources(ai)
    
    
    
    
    display_initial_candidate_resources(player, ai)
    
    #Player chooses a campaign strategy
    player_strategy = set_strategy()
    print(f"{STRINGS.PLAYER_STRATEGY} {player_strategy.title()}")
    log_strategy(player.name, player_strategy, player.points)
    ai_strategy=random.choice(CONSTANTS.STRATEGIES)
    log_strategy(ai.name, ai_strategy, ai.points)
    print(f"{STRINGS.AI_STRATEGY} {ai_strategy.title()}")
    

    #Simulate elections for 5 weeks
    for week in range(CONSTANTS.ROUND_WEEKS):
        print(f"{STRINGS.LINES}")
        print(f"\{STRINGS.WEEK} {week + 1}:")
        logger_simulation.info(f"\{STRINGS.WEEK} {week + 1}:")
        print(f"\n{STRINGS.PLAYER_POINTS}{player.points} | {STRINGS.PLAYER_RESOURCESS} {player.resources.total_resources():}: {STRINGS.FINANCIAL} {player.resources.financial_resources}, {STRINGS.INFLUENCE}: {player.resources.influence_resources}, {STRINGS.INTERNAL}: {player.resources.internal_resources}")
        print(f"{STRINGS.AI_POINTS}{ai.points} | {STRINGS.AI_RESOURCESS} {ai.resources.total_resources():}: {STRINGS.FINANCIAL} {ai.resources.financial_resources}, {STRINGS.INFLUENCE}: {ai.resources.influence_resources}, {STRINGS.INTERNAL}: {ai.resources.internal_resources}")
        logger_simulation.info(f"{player.name}: {player.resources.total_resources()}")
        logger_simulation.info(f"{ai.name}: {ai.resources.total_resources()}")

        
        #PLAYER TURN++++++++++++++++++++++++++++++++++++++++++
        print(f"{STRINGS.PLAYER_TURN}\n")
        show_actions()
        # Player decides whether to take an action or let the random event happen
        decision = input({STRINGS.ACTION_QUESTION}).strip().lower()
        run_player_simulation(player, player_strategy, decision)
        
        #AI'S TURN
        print(f"\n {STRINGS.AI_TURN} \n")
        time.sleep(3)
        
        run_ai_simulation(ai, ai_strategy)

        time.sleep(4)
        
        print(f"{STRINGS.LINES}")
    
    
    
    #END OF GAME
    print(f"\n{STRINGS.FINAL_SCORE}{player.name}: {player.points}")
    print(f"{STRINGS.FINAL_SCORE}{ai.name}: {ai.points}")
    logger_simulation.info(f"{STRINGS.PLAYER_POINTS} {player.points} ; {STRINGS.AI_POINTS} {ai.points}") 
    final_score_msg(player.points, ai.points)
    logger_simulation.info(f"{STRINGS.GAME_OVER}")
    

###############################################################
def main():
    
    """Main function to handle the menu and game flow."""
    while True:
        game_choice = intro_menu_option()

        if game_choice == "new_game":
            run_game()
    
    


 
###################################################################3    
if __name__=="__main__":
    main()