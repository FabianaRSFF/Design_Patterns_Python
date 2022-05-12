"""
Composite é um padrão de projeto estrutural que permite que 
você utilize a composição para criar objetos em estrutura de 
árvores. O padrão permite aos clientes tratarem de maneira 
uniforme objetos individuais (Leaf) e composição de objetos.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from mimetypes import init
from typing import List

class BoxStructure(ABC):
    """ Component """
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None:pass
    def remove(self, child: BoxStructure) -> None:pass


class Box(BoxStructure):
    """ Composite """
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []


    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """ Leaf """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
         print(self.name, self.price)

 
    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    """ Leaf """
    tshirt1 = Product('tshirt1', 19.9)
    tshirt2 = Product('tshirt2', 29.9)
    tshirt3 = Product('tshirt3', 39.9)
    tshirt4 = Product('tshirt4', 49.9)

    """ Composite"""
    tshirt_box = Box('tshirt_box')
    tshirt_box.add(tshirt1)
    tshirt_box.add(tshirt2)
    tshirt_box.add(tshirt3)
    tshirt_box.add(tshirt4)
    tshirt_box.add(tshirt1)
    tshirt_box.print_content()

    """ Leaf """
    smartphone1 = Product('smartphone1', 5999.9)
    smartphone2 = Product('smartphone2', 6999.9)
    smartphone3 = Product('smartphone3', 7999.9)
    smartphone4 = Product('smartphone4', 8999.9)
    """ Composite"""
    smartphone_box = Box('smartphone_box')
    smartphone_box.add(smartphone1)
    smartphone_box.add(smartphone2)
    smartphone_box.add(smartphone3)
    smartphone_box.add(smartphone4)
    smartphone_box.print_content()
    print(smartphone_box.get_price())

    """ Composite"""
    big_box = Box('big_box')
    big_box.add(tshirt_box)
    big_box.add(smartphone_box)
    big_box.print_content()
    print(big_box.get_price())
