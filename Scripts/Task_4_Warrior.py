
from __future__ import annotations
from Task_3_items import Weapon
from Task_1_Characters import Character


class Warrior(Character):
    """A defensive class with armour that reduses all damage taken"""
    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
        armor: int = 5,
    )-> None:
        """
        Initialise the Warrior
    
        Args:
            name, hp_max, damage, weapon: See Character.
            armor (int): Damage subtracted from every incoming hit
            (default = 5)
        """
        super().__init__(name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> int:
        """Reduce damage taken by amount of armor (never below 0), then apply it."""
        if amount < 0:
            raise ValueError("Damage cannot be negative.")
        return super().take_damage(max(amount - self.armor, 0))
