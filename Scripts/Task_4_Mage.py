
from __future__ import annotations
from Task_3_items import Weapon
from Task_1_Characters import Character


class Mage(Character):
    """A resource-based attacker: spells cost mana, but hit twice as hard."""

    SPELL_COST = 10 # Mana spent per spell
    SPELL_MULTIPLIER = 2 # Spell damage = base damage * spell multiplier
    MANA_REGEN = 5 # Mana restored when using base attack

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
        mana: int = 30,
        mana_max: int = 30,
    ) -> None:
        """
        Initialise the Mage
            
        Args:
            name, hp_max, damage, weapon: See Character.
            mana (int): Current mana (default = 30)
            mana_max (int): Max mana (default = 30)
        """
        
        super().__init__(name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.mana_max = mana_max
        self._mana = max(0, min(mana, mana_max))

    @property
    def mana(self) -> int:
        """Read only: Mage's current mana """
        return self._mana

    def attack (self, target: Character) -> int:
        """
        Cast spell if there is enough mana, if not: 
        base attack and retore mana

        Returns: 
            int: how much hp the targer actually lost
        """
        if self._mana >= self.SPELL_COST:
            self._mana -= self.SPELL_COST
            return target.take_damage(self.damage * self.SPELL_MULTIPLIER)

        self._mana = min(self._mana + self.MANA_REGEN, self.mana_max)
        return super().attack(target)
