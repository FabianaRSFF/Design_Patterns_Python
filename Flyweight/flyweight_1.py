"""
Padrão de projeto estrutural que tem a intenção de usar compartilha-
mento para suportar eficientemente grandes quantidades de 
objetos de forma granular.

Só use este método quando todas as condições seguintes forem
verdadeiras:
- uma aplicação utiliza uma grande quantidade de objetos;
- os custos de armazenamento são altos por causa da grande quan-
tidade de objetos;
- a maioria dos estados de objetos podem se tornar extrínsecos;
- muitos objetos podem ser substituídos por poucos objetos compar-
tilhados;
- a aplicação não depende da identidade dos objetos.

"""

from __future__ import annotations
from typing import Dict, List


class Client:
    """ Context """
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []
        """ Extrinsic address data: """
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address)-> None:
        self._addresses.append(address)

    def list_addresses(self)-> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    """ Flyweight """

    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code
        
    def show_address(self, address_number: str, address_details: str)-> None:
        print(
            self._street, address_number, address_details, self._neighbourhood, self._zip_code

        )

class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs)-> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs)-> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado.')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto.')

        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av Brasil', 
        neighbourhood= 'Centro',
        zip_code= '00000-000')

    a2 = address_factory.get_address(
        street='Av Brasil', 
        neighbourhood= 'Centro',
        zip_code= '00000-000')

    luiz = Client('Luiz')
    luiz.address_number = '500'
    luiz.address_details = 'casa'
    luiz.add_address(a1)
    luiz.list_addresses()

    janja = Client('Janja')
    janja.address_number = '500'
    janja.address_details = 'casa'
    janja.add_address(a2)
    janja.list_addresses()
    # teste