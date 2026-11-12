"""Items that characters can hold"""
from Task_2_Dice import Dice

class Weapon:
    """A weapon with damage decided by a dice roll"""

    def __init__(self,
        name: str,
        damage_dice: Dice
        ) -> None:
        """
        Initialise weapon
        
        Args:
            name: The name of the weapon, example "Spear"
            damage_dice: The dice rolled to determine damage.
        """
        self.name = name
        self.damage_dice = damage_dice