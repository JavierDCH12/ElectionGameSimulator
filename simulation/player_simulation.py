
from simulation.game import simulate_election
from simulation.resources import add_resources
from simulation.user_decisions import apply_action, select_action


def run_player_simulation(player, player_strategy):
    decision = input("Do you want to take an action this week? ").strip().lower()

    if decision == "yes":
            action = select_action()  
            can_apply = apply_action(player, action)  

            if not can_apply:
                print(f"Insufficient resources for action '{action.name}'. A random event will occur instead.\n")
                player.points = simulate_election(player, player.points, is_player=True, strategy=player_strategy)
                add_resources(player)
            else:
                print("x")

    else:
        print("\nNo action taken.")
        print("You saved resources and increased them.")
        print("A random event will occur.\n")
        player.points = simulate_election(player, player.points, is_player=True, strategy=player_strategy)
        add_resources(player)