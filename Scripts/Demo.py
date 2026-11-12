"""Demo of the battle simulator."""

import random

from Task_5_Battles import Battle
from Task_1_4_Characters import Mage, Warrior
from Task_2_Dice import Dice
#from Task_3_items import Weapon (will be added later)

def make_warrior() -> Warrior:
    """Create a fresh warrior with a sword."""
    return Warrior(
        "Gimli",
        hp_max=120,
        damage=10,
        weapon=Weapon("Sword", Dice(sides=8)),
        armor=5,
    )


def make_mage() -> Mage:
    """Create a fresh mage with a staff."""
    return Mage(
        "Gandalf",
        hp_max=80,
        damage=10,
        weapon=Weapon("Staff", Dice(sides=6)),
    )
