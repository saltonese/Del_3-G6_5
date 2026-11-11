import random

class Dice:
    """Represents n-sided dice"""

    def __init__(self, sides: int = 6) -> None:
        if sides < 2:
            raise ValueError( f"A dice need at least 2 sides, got{sides} ")
        self._sides = sides #protected: should not change after creation

    @property
    def sides(self) -> int:
        """Read only: number of sides on the dice"""
    

    def roll(self) -> int:
        """Roll the dice and return a number between 1 and sides"""


    def __call__(self) -> int:
        """Make the dice calleble so d20() does the same as d20.roll() """


    def __repr__(self) -> str:
        """represantasion of the dice, example. Dice(sides=6)"""
        return f"Dice(sides={self.sides})"