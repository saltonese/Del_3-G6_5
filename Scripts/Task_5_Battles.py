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

    def _attack(self, attacker: Character, target: Character) -> None:
        """Let attacker hit target and log the result."""
        damage = attacker.attack(target)
        self._log(
            f"{attacker.name} hits {target.name} for {damage} damage "
            f"({target.hp}/{target.hp_max} HP left)"
        )

    def play_round(self) -> None:
        """The hero attacks the enemy. If the enemy survives, it strikes back."""
        self.rounds_played += 1
        self._log(f"--- Round {self.rounds_played} ---")
        self._attack(self.hero, self.enemy)
        if self.enemy.is_alive:
            self._attack(self.enemy, self.hero)

    def simulate_battle(self, max_rounds: int = 1000) -> Character | None:
        """
        Play rounds until one character is no longer alive.

        Args:
            max_rounds (int): Safety limit, so a stalemate (e.g. two armored
                warriors who cannot hurt each other) does not loop forever.

        Returns:
            Character | None: The winner, or None if the limit was reached.
        """
        while (
            self.hero.is_alive
            and self.enemy.is_alive
            and self.rounds_played < max_rounds
        ):
            self.play_round()

        if self.hero.is_alive and self.enemy.is_alive:
            self._log(f"Stalemate after {self.rounds_played} rounds.")
            return None

        winner = self.hero if self.hero.is_alive else self.enemy
        self._log(f"{winner.name} wins after {self.rounds_played} rounds!")
        return winner
