import time


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
        opc=int(input("Choose an option: "))
        
        match opc:
            case 1:
                return "new_game"
            case 2:
                #show_options()
                return
            case 3:
                print("Exiting the game. Goodbye! ")
                return
            case _:
                print("Invalid option")
                time.sleep(2)
                
                