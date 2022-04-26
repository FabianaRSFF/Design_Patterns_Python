# Especificar os tipos de objetos a serem criados usando uma 
# intância-protótipo  e criar novos objetos pela cópia deste 
# protótipo.

# De acordo com o básico:
from __future__ import annotations
from typing import List


nome1 = 'Nome'
nome2 = nome1

nome1 = 'Outro Nome'
print(nome1)
print(nome2)

# As listas são mutáveis, portanto quando as duas apontarem para 
# o mesmo objeto, se uma for alterada, as outras também serão.

lista1 = [1, 2, 3]
lista2 = lista1

lista1.append(4)
print(lista1)
print(lista2)

class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()



class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str)-> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address)-> None:
        self.addresses.append(address)


class Address(StringReprMixin):
    def __init__(self, street: str, number:str) -> None:
        self.street = street
        self.number = number

if __name__ == '__main__':
    from copy import deepcopy
    fabi = Person('Fabi', 'Ladeira')
    endereco_fabi = Address('Av. Brasil', 2000)
    fabi.add_address(endereco_fabi)

    marido_fabi = deepcopy(fabi)
    marido_fabi.firstname = 'Rodrigo'

    print(fabi)
    print(marido_fabi)


