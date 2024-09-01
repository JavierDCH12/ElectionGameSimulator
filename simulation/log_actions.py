import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  

file_handler = logging.FileHandler('game_log.log')
file_handler.setLevel(logging.INFO)  

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def log_action(player_name, action_name, cost, benefit, resources):
    logger.info(f"Player: {player_name} | Action: {action_name} | Cost: {cost} | Benefit: {benefit} | Resources: {resources} | ")


def log_event(player_name, event_name, impact, score):
    logger.info(f"Player: {player_name} | Event Name: {event_name} | Impact: {impact} | Score: {score} | ")

def log_strategy(player_name, strategy_name, current_score):
    logger.info(f"Player: {player_name} | Strategy name: {strategy_name} | Current Score: {current_score}")