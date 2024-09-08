

class Event():
    
    def __init__(self, name, impact) -> None:
        self._name=name
        self._impact=impact
    
    @property
    def name(self):
        return self._name

    @property
    def impact(self):
        return self._impact
    
    @name.setter
    def name(self, value):
        self._name=value
    
    @impact.setter
    def impact(self, value):
        self._impact=value
    
    def trigger(self, politician):
        print(f"Event active: {self.name}")
        politician.points += self.impact  
        print(f"Event for {politician.name}: {'+' if self.impact >= 0 else ''}{self.impact} points")
    
    def __str__(self) -> str:
        return f"Event Name: {self.name} | Impact points: {self.impact}"