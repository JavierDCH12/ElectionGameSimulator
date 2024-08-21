

class Party():
    
    def __init__(self, name:str="", foundation_year:int="", lean:str="") -> None:
        self._name=name
        self._foundation_year=foundation_year
        self._lean=lean
    
    
    def __str__(self) -> str:
        return f"{self.name} ({self.lean}, founded in {self.year_of_foundation})"
        
        
        
        
        
        
        
        
        
        
        
        
        
        