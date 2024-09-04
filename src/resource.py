

class Resource():
    
    def __init__(self, financial_resources, influence_resources, internal_resources) -> None:
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
        return f"Total Resources: {self.total_resources()}"
        return f"Financial: {self.financial_resources} | Influence: {self.influence_resources} | Internal: {self.internal_resources}  "