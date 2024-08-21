from src.politician import Politician


from src import CONSTANTS


def main():
    
    yo = Politician("Yoshida", 30, "male", CONSTANTS.PARTY_LDP, CONSTANTS.AKITA)
    print(yo)
    
    
if __name__=="__main__":
    main()