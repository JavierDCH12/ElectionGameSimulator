import logging

from simulation.game import create_politician, create_ai_politician, simulate_election, set_initial_score, final_score_msg
from simulation.resources import set_initial_financial_resources, set_initial_internal_resources, set_initial_personal_resources, add_resources
from simulation.user_decisions import set_strategy, show_actions, apply_action, select_action, random_action
import src.CONSTANTS as CONSTANTS
from simulation.log_actions import log_action, log_event, log_strategy
import time
import os
import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  
file_handler = logging.FileHandler('logs/simulation.log')
file_handler.setLevel(logging.INFO)  
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)




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
    # Obtener los recursos totales para el jugador y el AI
    player_total_resources = (player.resources['financial'] +
                              player.resources['influence'] +
                              player.resources['internal'])
    ai_total_resources = (ai.resources['financial'] +
                          ai.resources['influence'] +
                          ai.resources['internal'])

    print("\nYour candidate:")
    print(f"{player}")
    print(f"Initial Score: {player.points}")
    print(f"Financial Resources: {player.resources['financial']} | "
          f"Influence Resources: {player.resources['influence']} | "
          f"Internal Resources: {player.resources['internal']}")
    print(f"Total Resources: {player_total_resources}")  # Total Resources
    time.sleep(2)
    
    print("\nA.I Candidate:")
    print(f"{ai}")
    print(f"Initial Score: {ai.points}")
    print(f"Financial Resources: {ai.resources['financial']} | "
          f"Influence Resources: {ai.resources['influence']} | "
          f"Internal Resources: {ai.resources['internal']}")
    print(f"Total Resources: {ai_total_resources}")  # Total Resources


###############################################################
def main():
    
    logger.info("Game starts\n")
    print_start_message()    
    
    player = create_politician() 
    logger.info(player)
    time.sleep(3)
    ai = create_ai_politician()
    logger.info(ai)
    time.sleep(2)
    
    #Set initial scores and resources
    player.points = set_initial_score(player)
    player.resources['financial'] = set_initial_financial_resources(player)
    player.resources['influence'] = set_initial_personal_resources(player)
    player.resources['internal'] = set_initial_internal_resources(player)

    ai.points = set_initial_score(ai)
    ai.resources['financial'] = set_initial_financial_resources(ai)
    ai.resources['influence'] = set_initial_personal_resources(ai)
    ai.resources['internal'] = set_initial_internal_resources(ai)
    
    
    display_initial_candidate_resources(player, ai)
    
    #Player chooses a campaign strategy
    player_strategy = set_strategy()
    log_strategy(player.name, player_strategy, player.points)
    ai_strategy=random.choice(CONSTANTS.STRATEGIES)
    log_strategy(ai.name, ai_strategy, ai.points)
    print(f"The AI has chosen the {ai_strategy.title()} strategy")
    

    #Simulate elections for 5 weeks
    for week in range(CONSTANTS.ROUND_WEEKS):
        print("--------------------------------------------------------------------------------------")
        print(f"\nWeek {week + 1}:")
        logger.info(f"\nWeek {week + 1}:")
        print(f"\nYOUR RESOURCES: {player.resources} | YOUR POINTS: {player.points}")
        print(f"AI RESOURCES: {ai.resources} | AI POINTS: {ai.points}")
        logger.info(f"{player.name}: {player.resources}")
        logger.info(f"{ai.name}: {ai.resources}")

        
        #PLAYER TURN++++++++++++++++++++++++++++++++++++++++++
        show_actions()
        # Player decides whether to take an action or let the random event happen
        decision = input("Do you want to take an action or let the week go by? (action/letgo): ")
        
        if decision == "action".strip().lower():
            action = select_action()  # Selects an action from available options
            apply_action(player, action)
            logger.info(f"Action taken: {action}")
        else:
            print("\nNo action taken.")
            print("You saved resources and increased them.")
            print("A random event will occur.\n")
            player.points = simulate_election(player, player.points, is_player=True, strategy=player_strategy)
            add_resources(player)
            
        #AI TURN++++++++++++++++++++++++++++++++++++++++++
        print("\nAI's TURN\n")
        time.sleep(3)
        ai_action=random_action(ai)
        if ai_action is not None:
            apply_action(ai, ai_action)
        else:
            add_resources(ai)
            ai.points = simulate_election(ai, ai.points, is_player=False, strategy=ai_strategy)  
        time.sleep(4)
        logger.info(f"{player.name}: {player.points}")
        logger.info(f"{ai.name}: {ai.points}")

        
        
        print("--------------------------------------------------------------------------------------")

    print(f"\nFinal Score for {player.name}: {player.points}")
    print(f"Final Score for {ai.name}: {ai.points}")
    logger.info(f"Player points: {player.points} ; Ai points: {ai.points}")
    
    final_score_msg(player.points, ai.points)
    logger.info("Game over")





 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
###################################################################3    
if __name__=="__main__":
    main()