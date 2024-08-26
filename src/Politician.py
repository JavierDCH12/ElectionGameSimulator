from src.party import Party
from src.prefecture import Prefecture


class Politician:
    
    def __init__(self, name: str = "", age: int = 0, gender: str = "", experience:str="", points:int=0, resources:int=0,
                 party = None, prefecture = None) -> None:
        self._name = name
        self._age = age
        self._gender = gender
        self._experience=experience
        self._points=points
        self._resources = {
            'financial': 0,
            'influence': 0,
            'internal': 0
        }
        self._party = party
        self._prefecture = prefecture
        
    
    # GETTERS
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def gender(self):
        return self._gender
    
    @property
    def experience(self):
        return self._experience
    
    @property
    def points(self):
        return self._points
    
    @property
    def resources(self):
        return self._resources
    
    @property
    def party(self):
        return self._party
    
    @property
    def prefecture(self):
        return self._prefecture
    
    # SETTERS
    @name.setter
    def name(self, value):
        self._name = value
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 25:
            self._age = value
        else:
            raise ValueError("The age must be a positive integer over 25 years old.")
        
    @gender.setter
    def gender(self, value):
        if value in ["Male", "Female"]:
            self._gender = value
        else:
            raise ValueError("Gender must be 'Male' or 'Female'")
    
    @experience.setter
    def experience(self, value):
        if value in ["Incumbent", "New candidate"]:
            self._experience = value
        else:
            raise ValueError("Experience must be 'Incumbent' or 'New candidate'")
    
        
    @party.setter
    def party(self, value):
        if isinstance(value, Party):    
            self._party = value
        else:
            raise ValueError("The party must be an instance of the Party class.")
        
    @prefecture.setter
    def prefecture(self, value):
        if isinstance(value, Prefecture):
            self._prefecture = value
        else:
            raise ValueError("The prefecture must be an instance of the Prefecture class.")
    
    def __str__(self) -> str:
        return (f"Name: {self.name} | Age: {self.age} | Gender: {self.gender} | "
                f"Political Party: {self.party.name} | Prefecture: {self.prefecture.name}"
                f"Points: {self.points} || Resources: {self.resources}"
                )
        
        
        

