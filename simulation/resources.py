from src.politician import Politician
from src import CONSTANTS
import random
from simulation import game

def set_initial_financial_resources(politician: Politician):
    #Financial Resources
    party = politician.party.name

    base_value = CONSTANTS.PARTY_POPULARITY_BONUS.get(party, 0)
    
    if base_value > 0:
        if party == CONSTANTS.PARTY_LDP.name or party == CONSTANTS.PARTY_CDPJ.name: 
            financial_resources = base_value + (base_value * 0.5)
        elif party ==CONSTANTS.PARTY_JCP.name or party == CONSTANTS.PARTY_KOMEITO.name:
            financial_resources = base_value + (base_value * 0.3)
        else:
            financial_resources = base_value
    else:
        financial_resources = 0  
    return financial_resources


def set_initial_personal_resources(politician: Politician):
    # Personal Influence Resources
    age_score = game.age_bonus(politician)

    experience_modifier = CONSTANTS.EXPERIENCE_LEVEL_MODIFIER.get(politician.experience, 1)
    influence_resources = round(experience_modifier * random.uniform(0.2, 0.4) * age_score)
    return influence_resources


def set_initial_internal_resources(politician: Politician):
     
    # Internal_resources
    party = politician.party.name
    base_value = CONSTANTS.PARTY_POPULARITY_BONUS.get(party, 0)
    if base_value > 0:
        if party == CONSTANTS.PARTY_JCP.name or party== CONSTANTS.PARTY_KOMEITO.name:
            internal_resources = base_value + (base_value * 0.3)
        elif party == CONSTANTS.PARTY_LDP.name:
            internal_resources = base_value + (base_value * 0.2)
        elif party == CONSTANTS.PARTY_CDPJ.name:
            internal_resources = base_value + (base_value * 0.1)
        else:
            internal_resources = base_value
    else:
        internal_resources = 0  
    
    return internal_resources
