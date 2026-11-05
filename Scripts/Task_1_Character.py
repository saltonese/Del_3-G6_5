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
        self.hp_max = hp.max    #protected: Only dameged via take_damage() / heal()
        self.damage = damage


    #properties

    @property
    def hp(self) -> int: 
        """Read only property to view HP without allowing direct edits"""        
        return self.hp

    @property
    def is_alive(self) -> bool:
        """Read only property: True if the character has any HP left"""
        return self.hp > 0


    
