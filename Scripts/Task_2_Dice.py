
import random

"""Dice used to introduce randomness into the game."""

class Dice:
    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the Dice

        Args:
            sides (int): Number of sides, must be at least 2 (default = 6)

        Raises:
            ValueError: If sides is smaller than 2.
        """
        if sides < 2:
            raise ValueError(f"A dice need at least 2 sides, got {sides}")
        self._sides = sides  # protected: should not change after creation

    @property
    def sides(self) -> int:
        """Read only: number of sides on the dice"""
        return self._sides

    def roll(self) -> int:
        """Roll the dice and return a number between 1 and sides"""
        return random.randint(1, self._sides)

    def __call__(self):
        """Make the dice callable, so d20() does the same as d20.roll()."""
        return self.roll()

    def __repr__(self) -> str:
        """Representation of the dice, example. Dice(sides=6)"""
        return f"Dice(sides={self._sides})"


