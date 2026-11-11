"""Characters for the RPG battle simulator: Character, Warrior and Mage."""

# lets us use "Character" as a type hint inside the Character class itself. 


from __future__ import annotations



class Character:
    """Repersents a character in the rpg"""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,

    ) -> None:
        """
        Initialise the Character
 
        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Base damage dealt when the character attacks
                without a weapon (default = 10)
            weapon (Weapon | None): Optional weapon. If equipped, the weapon's
                dice decide the damage instead of the base damage
    
        """
        self.name = name
        self._hp = hp_max     #protected: Only dameged via take_damage() / heal()
        self.hp_max = hp_max    
        self.damage = damage


    #properties

    @property
    def hp(self) -> int: 
        """Read only property to view HP without allowing direct edits"""        
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read only property: True if the character has any HP left"""
        return self._hp > 0


#------------------------------------------------------------------------------
# Actions   
    def take_damage(self, amount: int) -> int:
        """
        Reduce the chracters HP. HP is never less than 0
        
        Args:
            amount (int): incoming damage (cant be nagative)
        Returns:
            int: How much HP the character has lost
        """
        if amount < 0:
            raise ValueError("Damage cannot be negative")
        hp_before = self._hp
        self._hp = max(self._hp - amount, 0)
        return hp_before - self._hp


    def heal(self, amount: int) -> int:
        """
        Increase the character hp. HP never more than HP_max
        A dead character cannot be healed.
        
        Args:
            amount (int): How many hp to restore (cannot be nagative)
        Return:
            int: How much HP was restored.
        """
        
        if amount < 0:
            raise ValueError ( "Healing cannot be nagative")
        if not self.is_alive:
            return 0
        hp_before = self._hp
        self._hp = min(self._hp + amount, self.hp_max)
        return self._hp - hp_before

    def introduce(self) -> None:
        """Pritns a string that introduces the character"""
        print(f"I am the mighty {self.name}!")