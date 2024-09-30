from src.cons import CONSTANTS
from src.cons import INTS

import random
from simulation import game
from src.politician import Politician


def set_initial_financial_resources(politician: Politician):
    #Financial Resources
    party = politician.party.name

    base_value = CONSTANTS.PARTY_POPULARITY_BONUS.get(party, 0)
    
    if base_value > 0:
        if party == CONSTANTS.PARTY_LDP.name or party == CONSTANTS.PARTY_CDPJ.name: 
            financial_resources = base_value + (base_value * INTS.FINANCIAL_TOP_MODIFIER)
        elif party ==CONSTANTS.PARTY_JCP.name or party == CONSTANTS.PARTY_KOMEITO.name:
            financial_resources = base_value + (base_value * INTS.FINANCIAL_BOTTOM_MODIFIERI)
        else:
            financial_resources = base_value
    else:
        financial_resources = 0  
    return round(financial_resources)


def set_initial_personal_resources(politician: Politician):
    # Personal Influence Resources
    age_score = game.age_bonus(politician)

    experience_modifier = CONSTANTS.EXPERIENCE_LEVEL_MODIFIER.get(politician.experience, 1)
    influence_resources = round(age_score+ (experience_modifier * random.uniform(0.8, 1) * age_score)) 
    return round(influence_resources)


def set_initial_internal_resources(politician: Politician):
     
    # Internal_resources
    party = politician.party.name
    base_value = CONSTANTS.PARTY_POPULARITY_BONUS.get(party, 0)
    if base_value > 0:
        if party == CONSTANTS.PARTY_JCP.name or party== CONSTANTS.PARTY_KOMEITO.name:
            internal_resources = base_value + (base_value * INTS.INTERNAL_TOP_MODIFIER)
        elif party == CONSTANTS.PARTY_LDP.name:
            internal_resources = base_value + (base_value * INTS.INTERNAL_MIDDLE_MODIFIER)
        elif party == CONSTANTS.PARTY_CDPJ.name:
            internal_resources = base_value + (base_value * INTS.INTERNAL_BOTTOM_MODIFIER)
        else:
            internal_resources = base_value
    else:
        internal_resources = 0  
    
    return round(internal_resources)

def add_resources(politician:Politician): #Add resources when action is not taken
    politician.resources.financial_resources +=INTS.SAVE_RESOURCES
    politician.resources.influence_resources +=INTS.SAVE_RESOURCES
    politician.resources.internal_resources +=INTS.SAVE_RESOURCES