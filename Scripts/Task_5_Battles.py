"""Turn-based combat between two characters."""

from __future__ import annotations

from Task_1_4_Characters import Character

class Battle:
    """Manages a turn-based battle between a hero and an enemy."""

    def __init__(
        self, hero: Character, enemy: Character, verbose: bool = True
    ) -> None:
        """
        Initialise the Battle

        Args:
            hero (Character): The character who attacks first each round.
            enemy (Character): The opponent.
            verbose (bool): Print a log of the battle (default = True).
                Set to False when simulating many battles.
        """
        self.hero = hero
        self.enemy = enemy
        self.verbose = verbose
        self.rounds_played = 0

    def _log(self, message: str) -> None:
        """Print message if the battle is verbose."""
        if self.verbose:
            print(message)
