import logging
from src.politician import Politician
from src.action import Action
from src import CONSTANTS
from simulation.log_actions import log_action, log_strategy


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)  
file_handler = logging.FileHandler('errors.log')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def set_strategy(): #Set an initial strategy
    print(f"\n{CONSTANTS.STRATEGIES}")
    while True:
        
        strategy = input("Which kind of political strategy do you want to follow in this campaign? ").strip().lower()
        

        if strategy in CONSTANTS.STRATEGIES:
            print(f"You have chosen the {strategy.title()} strategy.")
            print("The chosen strategy will either intensify or dampen the impact of the random events, accordingly\n")
            return strategy
        else:
            print("You have to choose a valid campaign strategy: ")

def apply_strategy_modifiers(strategy, event_impact):
    original_impact = event_impact  

    if strategy == "aggressive campaign":
        if event_impact > 0:
            event_impact *= 1.2
            print(f"(Original impact: {original_impact}, Modified impact: {round(event_impact)})") #CHANGES THE IMAPCT OF THE RANDOM EVENT
                                                                                                    #INCREASE OR DECREASE
        else:
            event_impact *= 1.2
            print(f"(Original impact: {original_impact}, Modified impact: {round(event_impact)})")
    elif strategy == "defensive campaign":
        if event_impact > 0:
            event_impact *= 0.8
            print(f"(Original impact: {original_impact}, Modified impact: {round(event_impact)})")
        else:
            event_impact *= 0.8
            print(f"(Original impact: {original_impact}, Modified impact: {round(event_impact)})")
    
    # No message needed for neutral strategy since no modification is applied
    return round(event_impact)


def show_actions():
    print("\nYou can choose an action for this week:")
    for idx, action in enumerate(CONSTANTS.ACTIONS): #Showing the actions
        print(f"{idx + 1}. {action}")
    

def select_action():
    while True:
        try:
            choice = int(input("Enter the number of your choice: ")) - 1
            if 0 <= choice < len(CONSTANTS.ACTIONS):
                return CONSTANTS.ACTIONS[choice]
            else:
                print("Invalid choice. Please select a valid action number.")
                logger.warning(f"\nInvalid input for age: {choice}\n", exc_info=True)
        except ValueError:
            print("Please enter a valid number.")


def random_action(ai:Politician):
    affordable_actions = [
        action for action in CONSTANTS.ACTIONS 
        if all(ai.resources[resource] >= cost for resource, cost in action.cost.items())
    ]
    
    if not affordable_actions:  #We check if AI has resources to spend
        print("AI has no affordable actions.")
        return None

    
    best_action = max(affordable_actions, key=lambda a: a.benefit / sum(a.cost.values()))

    return best_action
    

def apply_action(politician: Politician, action: Action):
   
    can_afford = True
    for resource_type, cost in action.cost.items():
        if politician.resources[resource_type] < cost:
            can_afford = False
            break

    if can_afford:
        for resource_type, cost in action.cost.items():
            politician.resources[resource_type] -= cost
        politician.points += action.benefit
        
        log_action(politician.name, action.name, action.cost, action.benefit, politician.resources)
        print(f"{action.name} applied successfully! Points gained: {action.benefit}")
    else:
        print(f"Not enough resources to apply {action.name}.")