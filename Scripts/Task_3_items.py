from Task_2_Dice.py import Dice

class Weapon:
    def __init__(self, name, damage_dice: Dice):
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        return self.damage_dice.roll()


sword = Weapon("Sword", Dice(6))
print(sword.roll_damage())
