

class Resource():
    
    def __init__(self, financial_resources: int = 0, influence_resources:int=0, internal_resources:int=0) -> None:
        
        self._financial_resources=financial_resources
        self._influence_resources=influence_resources
        self._internal_resources=internal_resources
    
    @property
    def financial_resources(self):
        return self._financial_resources
    
    @property
    def influence_resources(self):
        return self._influence_resources
    
    @property
    def internal_resources(self):
        return self._internal_resources
    
    @financial_resources.setter
    def financial_resources(self, value):
        self._financial_resources=value
    
    @influence_resources.setter
    def influence_resources(self, value):
        self._influence_resources=value
    
    @internal_resources.setter
    def internal_resources(self, value):
        self._internal_resources=value
    
    
    def total_resources(self):
        return self.financial_resources+self.influence_resources+self.internal_resources
    
    def __str__(self) -> str:
        return (
            f"Total Resources: {self.total_resources()}\n"
            f"Financial: {self.financial_resources} | Influence: {self.influence_resources} | Internal: {self.internal_resources}"
    )
        
    def add(self, financial:int, influence: int, internal:int):
        self._financial_resources+=financial
        self._influence_resources+=influence
        self._internal_resources+=internal
    
    
    def subtract(self, financial: int = 0, influence: int = 0, internal: int = 0):
        """Subtracts resources from the current values, ensuring no negative resources."""
        if self.financial >= financial and self.influence >= influence and self.internal >= internal:
            self.financial -= financial
            self.influence -= influence
            self.internal -= internal
        else:
            raise ValueError("Insufficient resources to perform this operation. Limit 0")
    
        