
from src import CONSTANTS
def set_strategy():
    
    while True:
        
        strategy = input("Which kind of political strategy do you want to follow in this campaign? ").strip().lower()
        print(CONSTANTS.STRATEGIES)
        
        if strategy in CONSTANTS.STRATEGIES:
            print(f"You have chosen the {strategy.title()} strategy.")
            return strategy
        else:
            print("You have to choose a valid campaign strategy: ", CONSTANTS.STRATEGIES)

def apply_strategy_modifiers(strategy, event_impact):
    if strategy == "aggressive campaign":
        if event_impact > 0:
            event_impact *= 1.2
        else:
            event_impact *= 1.2
    elif strategy == "defensive campaign":
        if event_impact > 0:
            event_impact *= 0.8
        else:
            event_impact *= 0.8
    # No need for else, if it's neutral campaign, just return the original impact
    return event_impact