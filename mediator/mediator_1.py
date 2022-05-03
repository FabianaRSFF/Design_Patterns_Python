"""
Padrão de projeto comportamental que tem  a intenção de definir
um objeto que encapsula a forma como um conjunto de objetos
interage. O mediador promove o baixo acoplamento ao evitar que 
os objetos se refiram uns aos outros explicitamente e permite variar
suas interações independentemente
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self):
        self.name = str

    @abstractmethod
    def broadcast(self, msg: str) -> None: pass

    @abstractmethod
    def direct(self, msg: str) -> None: pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receveir: Colleague, msg: str)-> None:
        self.mediator.direct(self, receveir, msg)


    def direct(self, msg: str) -> None:
        print(msg)
        

class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str)-> None: pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver:str, msg: str)-> None: pass


class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague)-> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str)-> None:
        if not self.is_colleague(colleague):
            return

        print(f'{colleague.name} disse: {msg}')

    def direct(self, sender: Colleague, receiver:str, msg: str)-> None:
        if not self.is_colleague(sender):
            return

        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}'
        )

if __name__ =='__main__':
    chat = Chatroom()

    lula = Person('Lula', chat)
    dilma = Person('Dilma', chat)
    benedita = Person('Benedita', chat)
    haddad = Person('Haddad', chat)

    chat.add(lula)
    chat.add(dilma)
    chat.add(benedita)
    chat.add(haddad)

    benedita.broadcast('Olá companheiros e companheiras! \U0001F496')
    dilma.broadcast('Olá companheiros e companheiras! \U0001F496')
    haddad.broadcast('Olá companheiros e companheiras! \U0001F496')
    lula.broadcast('Olá companheiros e companheiras! \U0001F496')
    lula.broadcast('Preparados pra vitória? \U0001F496')
    benedita.broadcast('Lula Já! \U0001F496')
    dilma.broadcast('Lula Já! \U0001F496')
    haddad.broadcast('Lula Já! \U0001F496')

    print()
    lula.send_direct('Benedita', 'Já ganhamos Bené!')
    dilma.send_direct('Benedita', 'Já ganhamos Bené! Lula Já!\U0001F496')