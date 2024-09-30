
from simulation.game import generate_score
from simulation.resources import add_resources
from simulation.user_decisions import apply_action, select_action
from src.cons import STRINGS


def run_player_simulation(player, player_strategy, decision):
    

    if decision == "yes":
            action = select_action()  
            can_apply = apply_action(player, action)  

            if not can_apply:
                print(f"{STRINGS.NOT_ENOUGH_RES_2}'{action.name}'. {STRINGS.RANDOM_EVENT}\n")
                player.points = generate_score(player, player.points, is_player=True, strategy=player_strategy)
                add_resources(player)

    else:
        print(f"\n{STRINGS.NO_ACTION}")
        print(f"{STRINGS.RESOURCES_SAVED}")
        print(f"{STRINGS.RANDOM_EVENT}\n")
        player.points = generate_score(player, player.points, is_player=True, strategy=player_strategy)
        add_resources(player)