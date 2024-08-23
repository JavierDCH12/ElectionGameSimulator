from src.politician import Politician
from src import  CONSTANTS
import random
from src import game


def set_initial_resources(politician: Politician):
    party = politician.party.name
    age_score=game.age_bonus(politician)
    
    if party == CONSTANTS.PARTY_LDP or CONSTANTS.PARTY_CDPJ: 
        financial_resources = CONSTANTS.PARTY_POPULARITY_BONUS.get(politician.party.name, 0) * 0.5
    elif party == CONSTANTS.PARTY_JCP or CONSTANTS.PARTY_KOMEITO:
            financial_resources = CONSTANTS.PARTY_POPULARITY_BONUS.get(politician.party.name, 0) * 0.25

    
    
    
    influence_resources = CONSTANTS.EXPERIENCE_LEVEL_MODIFIER.get(politician.experience, 1) * random(0.1, 0.3)  * age_score
    
    if party == CONSTANTS.PARTY_JCP or CONSTANTS.PARTY_KOMEITO:
        internal_resources = CONSTANTS.PARTY_POPULARITY_BONUS.get(politician.party.name, 0) * 0.3
    elif party == CONSTANTS.PARTY_LDP:
        internal_resources = CONSTANTS.PARTY_POPULARITY_BONUS.get(politician.party.name, 0) * 0.2
    elif party == CONSTANTS.PARTY_CDPJ:
        internal_resources = CONSTANTS.PARTY_POPULARITY_BONUS.get(politician.party.name, 0) * 0.1

    return financial_resources, influence_resources, internal_resources