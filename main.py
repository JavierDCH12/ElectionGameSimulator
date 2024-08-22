from src.politician import Politician
from simulation.game import create_politician, create_ai_politician, set_initial_score
from src import CONSTANTS
import time
import os

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
    print("Your candidate: ")
    score = set_initial_score(yo)
    print(f"{yo}: Score: {score}")
    
    print("\nA.I Candidate:")
    ai = create_ai_politician()
    ai_score = set_initial_score(ai)
    print(f"{ai}: Score: {ai_score}")
    
    
if __name__=="__main__":
    main()