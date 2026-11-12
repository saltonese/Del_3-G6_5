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
        weapon: Weapon | None = None
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
        self.weapon = weapon


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

    def _roll_attack_damage(self) -> int:
        """Base attack damage, weapons will be added later"""
        if self.weapon is None:
            return self.damage
        else:
            return self.weapon.roll_damage()

    def attack(self, target: Character,) -> int:
        """
        Attack the target by asking it to take damage.

        Returns:
        int: How many HP the target actually lost.
        """
        return target.take_damage(self._roll_attack_damage())

    def introduce(self) -> None:
        """Pritns a string that introduces the character"""
        print(f"I am the mighty {self.name}!")
#---------------------------------------------------------------
#spesical methods

    def __repr__(self) -> str:
        """Representation of character object"""
        return (
            f"<{type(self).__name__} name={self.name} hp={self.hp} "
            f"damage={self.damage}>"
        )

    def __str__(self) -> str:
        """String representation of character object"""
        return (
            f"{type(self).__name__}: {self.name} with {self.hp} HP "
            f"and {self.damage} damage"
        )


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
        super().__init__(name, hp_max=hp_max, damage=damage)
        self.armor = armor

    def take_damage(self, amount: int) -> int:
        """Reduce damage taken by amount of armor (never below 0), then apply it."""
        if amount < 0:
            raise ValueError("Damage cannot be negative.")
        return super().take_damage(max(amount - self.armor, 0))

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
        
        super().__init__(name, hp_max=hp_max, damage=damage)
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
