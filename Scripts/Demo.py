"""Demo of the battle simulator."""

import random

from Task_5_Battles import Battle
from Task_1_4_Characters import Mage, Warrior
from Task_2_Dice import Dice
from Task_3_items import Weapon

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


def win_rates(n_battles: int = 1000) -> dict[str, int]:
    """Simultaions of warrior (hero) vs mage (enemy) battles, counts wins"""

    wins = {"Warrior": 0, "Mage": 0, "Stalemate": 0}
    for _ in range (n_battles): 
        # Characters are damaged durning a battle, so create fresh ones
        winner = Battle(
            make_warrior(), make_mage(), verbose=False
        ).simulate_battle()
        key = "Stalemate" if winner is None else type(winner).__name__
        wins[key] += 1
    return wins

