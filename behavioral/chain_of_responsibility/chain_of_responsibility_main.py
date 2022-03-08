from __future__ import annotations
from typing import TYPE_CHECKING
from random import choice

from behavioral.chain_of_responsibility.data import Human
from behavioral.chain_of_responsibility.logic import Bravery, Diamond, Satiety, Fear, DefenseTeardown, Starvation

if TYPE_CHECKING:
    from behavioral.chain_of_responsibility.logic import BaseHandler


MODIFIERS = (Bravery, Diamond, Satiety, Fear, DefenseTeardown, Starvation)


def main() -> None:
    for _ in range(0, 5):
        human = Human(1, 1, 1)
        print(f"Before applying modifiers modification: {human}")
        chain = get_random_modifiers(human)
        chain.handle()
        print(f"After applying modifiers modification: {human}\n")


def get_random_modifiers(human: Human) -> BaseHandler:
    chain, previous_modifier = None, None
    applied_modifiers = []

    for _ in range(0, 3):
        while (random_modifier := choice(MODIFIERS)) in applied_modifiers:
            pass

        applied_modifiers.append(random_modifier)
        modifier = random_modifier(human)

        if previous_modifier is not None:
            previous_modifier.next_handler = modifier

        if chain is None:
            chain = modifier

        previous_modifier = modifier

    return chain


if __name__ == "__main__":
    main()
