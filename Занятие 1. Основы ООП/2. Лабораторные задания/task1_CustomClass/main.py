# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union

class Tanker:
    def __init__(self, capacity_volume: float, crew: int, occupied_volume: int):

        self.capacity_volume = capacity_volume
        self.crew = crew
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

class Bulker:
    def __init__(self, capacity_weight: float, crane:int, occupied_weight: int):

        self.capacity_weight = capacity_weight
        self.crane = crane
        self.occupied_weight = occupied_weight

if __name__ == "__main__":
        # TODO работоспособность экземпляров класса проверить с помощью doctest
        pass


class Tug_Supply:
    def __init__(self, hook_force: float, capacity_container, occupied_container):

        self.hook_force = hook_force
        self.capacity_container = capacity_container
        self.occupied_container = occupied_container