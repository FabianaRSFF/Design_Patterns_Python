"""
Padrão de projeto comportamental que tem a intenção de permitir
que você salve e restaure um estado anterior de um objeto ori-
ginator, sem revelar os detalhes de sua implementação e sem 
violar o encapsulamento.
Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armezenar mementos e também é usado com 
o Padrão Command.
"""
from __future__ import annotations
from typing import Dict, List
from copy import deepcopy

class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state', state)

    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, name, value):
        raise AttributeError('Sorry, I am immutable')


class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento)-> None:
        self.__dict__= memento.get_state()

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'


class Caretaker:
    def __init__(self, originator: ImageEditor):
        self._originator = originator
        self._mementos: List[Memento]=[]

    def backup(self)->None:
        self._mementos.append(self._originator.save_state())

    def restore(self)->None:
        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())
        


if __name__ == "__main__":
    img = ImageEditor('Vitória_PT_2022', 111, 111)
    caretaker = Caretaker(img)
    caretaker.backup()

    img.name = 'Vitória_PT_2022.jpg'
    img.width = 222
    img.height = 222
    caretaker.backup()

    img.name = 'Vitória_PT_2022.jpg'
    img.width = 333
    img.height = 333
    caretaker.backup()

    img.name = 'Vitória_PT_2022.jpg'
    img.width = 444
    img.height = 444
    

    caretaker.restore()
    

    print(img)