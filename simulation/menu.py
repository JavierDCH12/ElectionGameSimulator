import time
import logging
logger_error = logging.getLogger(__name__)
logger_error.setLevel(logging.ERROR)  
file_handler = logging.FileHandler('logs/errors.log')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger_error.addHandler(file_handler)



def intro_menu_option():
    
    while True:
        print("""
        ================================
        Welcome to Election Game Simulator
        ================================
        1. New Game
        2. Options
        3. Exit
        ================================
        """)
        try:
            
            opc=int(input("Choose an option: "))
            
            match opc:
                case 1:
                    return "new_game"
                case 2:
                    #show_options()
                    return
                case 3:
                    print("Exiting the game. Goodbye! ")
                    exit
                case _:
                    print("Invalid option")
                    time.sleep(2)
        except ValueError:
            print("You must enter a valid option (1-3)")
            logger_error.error(f"\nInvalid input for initial menu option: {opc}\n", exc_info=True)

            time.sleep(1)
                    
                