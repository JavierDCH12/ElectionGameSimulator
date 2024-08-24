
from src import CONSTANTS
def set_strategy():
    print(f"\n{CONSTANTS.STRATEGIES}")
    while True:
        
        strategy = input("Which kind of political strategy do you want to follow in this campaign? ").strip().lower()
        print(CONSTANTS.STRATEGIES)
        
        if strategy in CONSTANTS.STRATEGIES:
            print(f"You have chosen the {strategy.title()} strategy.")
            print("The chosen strategy will either intensify or dampen the impact of the random events, accordingly")
            return strategy
        else:
            print("You have to choose a valid campaign strategy: ")

def apply_strategy_modifiers(strategy, event_impact):
    original_impact = event_impact  

    if strategy == "aggressive campaign":
        if event_impact > 0:
            event_impact *= 1.2
            print(f"(Original impact: {original_impact}, Modified impact: {round(event_impact)})") #TODO CONTROLAR LOS DECIMALES
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
    return event_impact




