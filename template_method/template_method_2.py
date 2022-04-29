from abc import abstractmethod


"""
Template method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos para 
as subclasses por herança. Template method permite que subclasses
redefinam certos passos de um algoritmo sem mudar a estrutura do 
mesmo.

The Hollywood Principle: "Don't Call Us, We Call you."
"""
from abc import ABC, abstractmethod

class Pizza(ABC):
    # classe abstrata
    def prepare(self)-> None:
        # template_method
        self.hook_before_add_ingredients()
        self.add_ingredients() # abstract
        self.hook_after_add_ingredients()
        self.cook() # abstract
        self.cut() # Concrete
        self.serve() # Concrete

    def hook_before_add_ingredients(self)-> None: pass
    def hook_after_add_ingredients(self)-> None: pass
    

    def cut(self)-> None:
        print(f'{self.__class__.__name__}: Cuting the pizza.')

    def serve(self)-> None:
        print(f'{self.__class__.__name__}: Serving the pizza.')

    @abstractmethod
    def add_ingredients(self)-> None: pass
    
    @abstractmethod
    def cook(self)-> None: pass


class ALaMaison(Pizza):
    def add_ingredients(self)-> None:
        print(f'À La Maison - adding: bluecheese, muzzarela. ')

    def cook(self)-> None:
        print(f'À La Maison, cooking, time to prepare: 45 min.')


class Pepperonni(Pizza):
    def hook_before_add_ingredients(self)-> None:
        print(f'Going to Italy to buy pepperoni, in Brazil it is very expansive.')
    def add_ingredients(self)-> None:
        print(f'Pepperoni - adding: pepperoni, muzzarela. ')

    def cook(self)-> None:
        print(f'Pepperoni, cooking, time to prepare: 45 min.')



if __name__=='__main__':
    a_la_maison = ALaMaison()
    a_la_maison.prepare()

    print()
    pep = Pepperonni()
    pep.prepare()

