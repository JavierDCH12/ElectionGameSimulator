from src.politician import Politician
from src.action import Action
from src.cons import CONSTANTS
from src.cons import STRINGS

from simulation.log_actions import log_action




def set_strategy(): #Set an initial strategy
    
    print(f"\n{STRINGS.STRATEGIES}{', '.join(CONSTANTS.STRATEGIES)}")
    while True:
        
        strategy = input(f"{STRINGS.STRATEGY_QUESTION}").strip().lower()
        

        if strategy in CONSTANTS.STRATEGIES:
            print(f"{STRINGS.STRATEGY_CHOSEN} {strategy.title()}")
            print(f"{STRINGS.STRATEGY_EFFECT}\n")
            return strategy
        else:
            print(f"{STRINGS.STRATEGY_ERROR}")

def apply_strategy_modifiers(strategy, event_impact):
    original_impact = event_impact 
    multiplier=1 

    if strategy == "aggressive campaign":
        multiplier=1.2
    elif strategy == "defensive campaign":
        multiplier=0.8
        
    modified_impact=original_impact*multiplier
    
    return round(modified_impact) 
    


def show_actions():
    print(f"\n{STRINGS.CHOOSE_ACTION_1}")
    for idx, action in enumerate(CONSTANTS.ACTIONS): #Showing the actions
        print(f"{idx + 1}. {action}")
    

def select_action():
    while True:
        try:
            choice = int(input(f"{STRINGS.CHOOSE_ACTION_2}")) - 1
            if 0 <= choice < len(CONSTANTS.ACTIONS):
                return CONSTANTS.ACTIONS[choice]
            else:
                print(f"{STRINGS.ACTION_ERROR_1}")
        except ValueError:
            print(f"{STRINGS.ACTION_ERROR_2}")


def random_action(ai: Politician):
    affordable_actions = []
    for action in CONSTANTS.ACTIONS:
        if (ai.resources.financial_resources >= action.cost.get('financial', 0) and
            ai.resources.influence_resources >= action.cost.get('influence', 0) and
            ai.resources.internal_resources >= action.cost.get('internal', 0)):
            affordable_actions.append(action)

    if not affordable_actions:
        print(f"{STRINGS.NOT_ENOUGH_RES_1}")
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
        print(f"{STRINGS.ACTION_APPLIED}'{action.name}' {STRINGS.POINTS_WON} {action.benefit}")
        return True
    else:
        print(f"{STRINGS.NOT_ENOUGH_RES_2}'{action.name}'.")
        return False
