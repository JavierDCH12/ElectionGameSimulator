
from src import CONSTANTS

class Prefecture:
    
    def __init__(self, name:str="") -> None:
        self._name=name
        
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        
    def __str__(self) -> str:
        return f"Name: {self.name}"