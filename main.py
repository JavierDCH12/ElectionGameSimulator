from simulation.game import create_politician, create_ai_politician, simulate_election, set_initial_score, final_score_msg
import time
import os
import src.CONSTANTS as CONSTANTS

from simulation.resources import set_initial_financial_resources, set_initial_internal_resources, set_initial_personal_resources
from simulation.user_decisions import set_strategy, show_actions, apply_action, select_action

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
    time.sleep(3)
    
    print("\nA.I Candidate:")
    print(f"{ai}")
    print(f"Initial Score: {ai.points}")
    print(f"Financial Resources: {ai.resources['financial']} | "
          f"Influence Resources: {ai.resources['influence']} | "
          f"Internal Resources: {ai.resources['internal']}")
    print(f"Total Resources: {ai_total_resources}")  # Total Resources


###############################################################
def main():
    
    
    print_start_message()    
    
    player = create_politician()
    time.sleep(3)
    ai = create_ai_politician()
    time.sleep(2)
    
    # Set initial scores and resources
    player.points = set_initial_score(player)
    player.resources['financial'] = set_initial_financial_resources(player)
    player.resources['influence'] = set_initial_personal_resources(player)
    player.resources['internal'] = set_initial_internal_resources(player)

    ai.points = set_initial_score(ai)
    ai.resources['financial'] = set_initial_financial_resources(ai)
    ai.resources['influence'] = set_initial_personal_resources(ai)
    ai.resources['internal'] = set_initial_internal_resources(ai)
    
    
    display_initial_candidate_resources(player, ai)
    
    # Player chooses a campaign strategy
    player_strategy = set_strategy()
    

    # Simulate elections for 5 weeks
    for week in range(CONSTANTS.ROUND_WEEKS):
        print(f"\nWeek {week + 1}:")
        
        show_actions()
        # Player decides whether to take an action or let the random event happen
        decision = input("Do you want to take an action or let the week go by? (action/letgo): ").lower()
        
        if decision == "action":
            action = select_action()  # Selects an action from available options
            apply_action(player, action)
        else:
            print("No action taken. A random event will occur.")
            player.points = simulate_election(player, player.points, is_player=True, strategy=player_strategy)
        
        
        player.points = simulate_election(player, player.points, is_player=True, strategy=player_strategy)
        time.sleep(10)
        ai.points = simulate_election(ai, ai.points, is_player=False)  
        time.sleep(4)

    print(f"\nFinal Score for {player.name}: {player.points}")
    print(f"Final Score for {ai.name}: {ai.points}")
    
    final_score_msg(player.pointsa, ai.points)





 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
###################################################################3    
if __name__=="__main__":
    main()