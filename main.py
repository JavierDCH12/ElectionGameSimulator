from simulation.game import create_politician, create_ai_politician, simulate_election, set_initial_score
import time
import os
import src.CONSTANTS as CONSTANTS
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



###############################################################

def main():
    print_start_message()    
    
    yo = create_politician()
    ai = create_ai_politician()
    
    # Set initial scores
    yo_score = set_initial_score(yo)
    ai_score = set_initial_score(ai)

    print("Your candidate: ")
    print(f"{yo}: \nInitial Score: {yo_score}")

    print("\nA.I Candidate:")
    print(f"{ai}: \nInitial Score: {ai_score}")

    # Simulate elections for 5 weeks
    for week in range(CONSTANTS.ROUND_WEEKS):
        print(f"\nWeek {week + 1}:")
        yo_score = simulate_election(yo, yo_score, is_user=True)
        ai_score = simulate_election(ai, ai_score, is_user=False)
        time.sleep(4)

    print(f"\nFinal Score for {yo.name}: {yo_score}")
    print(f"Final Score for {ai.name}: {ai_score}")
    
if __name__=="__main__":
    main()