

class Action():
    
    def __init__(self, name, cost, benefit, description) -> None:
        self._name=name
        self._cost=cost
        self._benefit=benefit
        self._description=description
    
    
    @property
    def name(self):
        return self._name
    
    @property
    def cost(self):
        return self._cost
    
    @property
    def benefit(self):
        return self._benefit
    
    @property
    def description(self):
        return self._description
    
    
    @name.setter
    def name(self, value):
        self._name=value
        
    @cost.setter
    def cost(self, value):
        self._cost=value
        
    @benefit.setter
    def benefit(self, value):
        self._benefit=value
        
    @description.setter
    def description(self, value):
        self._description=value
    
    
    def __str__(self) -> str:
        return f"'{self.name}': Cost {self.cost} |  Benefit {self.benefit}"