from __future__ import annotations
from dataclasses import dataclass
from typing import List
from copy import deepcopy


# Ingredients
@dataclass
class Ingredient:
    price: float

@dataclass
class Bread(Ingredient):
    price:float = 1.99

@dataclass
class Sausage(Ingredient):
    price:float = 2.99

@dataclass
class Bacon(Ingredient):
    price:float = 4.99

@dataclass
class Egg(Ingredient):
    price:float = 1.99

@dataclass
class Cheese(Ingredient):
    price:float = 4.99

@dataclass
class MashedPotatos(Ingredient):
    price:float = 2.99

@dataclass
class PotatoSticks(Ingredient):
    price:float = 0.99

# Hotdogs
class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}({self.price}) -> ({self.ingredients})'

class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SimpleHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]

class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SpecialHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks(),
            MashedPotatos(),
            Bacon(),
            Egg(),
            Cheese()
        ]

# Decorators
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog) -> None:
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        return self.hotdog.price

    @property
    def name(self) -> str:
        return self.hotdog.name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self.hotdog.ingredients


class BaconDecorator(HotdogDecorator):
    def __init__(self, hotdog: Hotdog) -> None:
        super().__init__(hotdog)

        self._ingredient = Bacon()
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)


    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)


    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients




if __name__ == '__main__':
    simple_hotdog = SimpleHotdog()
    decoreted_simple_hotdog = HotdogDecorator(simple_hotdog)
    bacon_simple_hotdog = BaconDecorator(simple_hotdog)
    print(simple_hotdog)
    print(bacon_simple_hotdog)

    special_hotdog = SpecialHotdog()
    print(special_hotdog)
