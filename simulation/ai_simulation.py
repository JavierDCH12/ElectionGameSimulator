
from simulation.game import generate_score
from simulation.resources import add_resources
from simulation.user_decisions import apply_action, random_action

def run_ai_simulation(ai, ai_strategy):
    ai_action = random_action(ai)
    if ai_action is not None:
            can_apply_ai = apply_action(ai, ai_action)
            if not can_apply_ai:
                add_resources(ai)
                ai.points = generate_score(ai, ai.points, is_player=False, strategy=ai_strategy)
    else:
        add_resources(ai)
        ai.points = generate_score(ai, ai.points, is_player=False, strategy=ai_strategy)

        