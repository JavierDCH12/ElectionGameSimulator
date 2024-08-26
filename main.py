from simulation.game import create_politician, create_ai_politician, simulate_election, set_initial_score, final_score_msg
import time
import os
import src.CONSTANTS as CONSTANTS

from simulation.resources import set_initial_financial_resources, set_initial_internal_resources, set_initial_personal_resources
from simulation.user_decisions import set_strategy, show_actions

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


def display_initial_candidate_resources(player, player_score, player_financial_resources, player_influence_resources, player_internal_resources, ai, ai_score, ai_financial_resources, ai_influence_resources, ai_internal_resources):
    player_total_resources = player_financial_resources + player_influence_resources + player_internal_resources
    ai_total_resources = ai_financial_resources + ai_influence_resources + ai_internal_resources

    print("\nYour candidate: ")
    print(f"{player}")
    print(f"Initial Score: {player_score}")
    print(f"Financial Resources: {player_financial_resources} | Influence Resources: {player_influence_resources} | Internal Resources: {player_internal_resources}  ")
    print(f"Total Resources: {player_total_resources}")  #Total Resources
    time.sleep(3)
    print("\nA.I Candidate:")
    print(f"{ai}")
    print(f"Initial Score: {ai_score}")
    print(f"Financial Resources: {ai_financial_resources} | Influence Resources: {ai_influence_resources} | Internal Resources: {ai_internal_resources}  ")
    print(f"Total Resources: {ai_total_resources}")  #Total Resources


###############################################################
def main():
    
    show_actions()
    
    """print_start_message()    
    
    player = create_politician()
    time.sleep(3)
    ai = create_ai_politician()
    
    # Set initial scores and resources
    player_score = set_initial_score(player)
    player_financial_resources = set_initial_financial_resources(player)
    player_influence_resources = set_initial_personal_resources(player)
    player_internal_resources = set_initial_internal_resources(player)
    
    ai_score = set_initial_score(ai)
    ai_financial_resources = set_initial_financial_resources(ai)
    ai_influence_resources = set_initial_personal_resources(ai)
    ai_internal_resources = set_initial_internal_resources(ai)
    
    
    display_initial_candidate_resources(player, player_score, player_financial_resources, player_influence_resources, player_internal_resources, 
                                        ai, ai_score, ai_financial_resources, ai_influence_resources, ai_internal_resources)
    
    # Player chooses a campaign strategy
    player_strategy = set_strategy()
    show_actions()

    # Simulate elections for 5 weeks
    for week in range(CONSTANTS.ROUND_WEEKS):
        print(f"\nWeek {week + 1}:")
        player_score = simulate_election(player, player_score, is_player=True, strategy=player_strategy)
        time.sleep(10)
        ai_score = simulate_election(ai, ai_score, is_player=False)  
        time.sleep(4)

    print(f"\nFinal Score for {player.name}: {player_score}")
    print(f"Final Score for {ai.name}: {ai_score}")
    
    final_score_msg(player_score, ai_score)
"""
    




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
###################################################################3    
if __name__=="__main__":
    main()