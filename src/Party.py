
class Party:
    def __init__(self, name: str, foundation_year: int, lean: str) -> None:
        self._name = name
        self._foundation_year = foundation_year
        self._lean = lean

    @property
    def name(self) -> str:
        return self._name

    @property
    def foundation_year(self) -> int:
        return self._foundation_year

    @property
    def lean(self) -> str:
        return self._lean

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @foundation_year.setter
    def foundation_year(self, value: int) -> None:
        if 1950 <= value <= 2024:
            self._foundation_year = value
        else:
            raise ValueError("The foundation year must be between 1950 and 2024")

    @lean.setter
    def lean(self, value: str) -> None:
        valid_leans = ["right", "left", "liberal", "center"]
        if value in valid_leans:
            self._lean = value
        else:
            raise ValueError("The lean of the party must be one of the following: 'right', 'left', 'liberal', 'center'")

    def __str__(self) -> str:
        return f"{self.name} ({self.lean}, founded in {self.foundation_year})"
