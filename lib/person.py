from __future__ import annotations

from lib.object import Object


class Person(Object):
    class STATUS:
        ALIVE = "alive"
        DEAD = "dead"
        REPRODUCING = "reproducing"

    def __init__(self, id: str = None) -> None:
        super().__init__(id)
        self.food: float = 0

    def eat(self, totalFood: float, opponent: Person = None) -> None:
        if opponent is None:
            self.food += totalFood
        else:
            self.food += totalFood / 2

    def passDay(self) -> Person | None:
        food = self.food
        self.food = 0
        if food > 1:
            return self.STATUS.REPRODUCING

        if food == 0:
            return self.STATUS.DEAD

        return self.STATUS.ALIVE
