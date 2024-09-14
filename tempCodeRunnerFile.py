
    """Main function to handle the menu and game flow."""
    while True:
        game_choice = intro_menu_option()

        if game_choice == "new_game":
            run_game()
    
    


 
###################################################################3    
if __name__=="__main__":
    main()