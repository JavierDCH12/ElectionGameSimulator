import logging
from src.politician import Politician
from src.action import Action
from src import CONSTANTS
from simulation.log_actions import log_action, log_strategy


logger_error = logging.getLogger(__name__)
logger_error.setLevel(logging.ERROR)  
file_handler = logging.FileHandler('logs/errors.log')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger_error.addHandler(file_handler)

def set_strategy(): #Set an initial strategy
    
    print(f"\nStrategies: {', '.join(CONSTANTS.STRATEGIES)}")
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
    multiplier=1 

    if strategy == "aggressive campaign":
        multiplier=1.2
    elif strategy == "defensive campaign":
        multiplier=0.8
        
    modified_impact=original_impact*multiplier
    print(f"(Original impact: {original_impact}, Modified impact: {round(modified_impact)})")
    
    return round(modified_impact) 
    # No message needed for neutral strategy since no modification is applied
    return round(modified_impact)


def show_actions():
    print("\nChoose an action for this week:")
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
        except ValueError:
            print("Please enter a valid number.")


def random_action(ai: Politician):
    affordable_actions = []
    for action in CONSTANTS.ACTIONS:
        if (ai.resources.financial_resources >= action.cost.get('financial', 0) and
            ai.resources.influence_resources >= action.cost.get('influence', 0) and
            ai.resources.internal_resources >= action.cost.get('internal', 0)):
            affordable_actions.append(action)

    if not affordable_actions:
        print("AI has no affordable actions")
        return None

    best_action = max(affordable_actions, key=lambda a: a.benefit / sum(a.cost.values()))
    return best_action

    

def apply_action(politician: Politician, action: Action):
    can_afford = (
        politician.resources.financial_resources >= action.cost.get('financial', 0) and
        politician.resources.influence_resources >= action.cost.get('influence', 0) and
        politician.resources.internal_resources >= action.cost.get('internal', 0)
    )

    if can_afford:
        politician.resources.financial_resources -= action.cost.get('financial', 0)
        politician.resources.influence_resources -= action.cost.get('influence', 0)
        politician.resources.internal_resources -= action.cost.get('internal', 0)
        
        politician.points += action.benefit
        
        log_action(politician.name, action.name, action.cost, action.benefit, politician.resources)
        print(f"'{action.name}' applied! Puntos won: {action.benefit}")
        return True
    else:
        print(f"Not enough resources to apply '{action.name}'.")
        return False
