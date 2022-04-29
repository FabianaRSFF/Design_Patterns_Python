from abc import abstractmethod
from pipes import Template

"""
Template method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos para 
as subclasses por herança. Template method permite que subclasses
redefinam certos passos de um algoritmo sem mudar a estrutura do 
mesmo.

The Hollywood Principle: "Don't Call Us, We Call you."
"""
from abc import ABC, abstractmethod


class Abstract:
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self): pass

    def base_class_method(self):
        print("Hi, I'm from abstract class and I will be played.")


    @abstractmethod
    def operation1(self): pass

    @abstractmethod
    def operation2(self): pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('I am using a hook.')

    def operation1(self):
        print('Mission 1 accomplished.')

    def operation2(self):
        print('Mission 2 accomplished.')


class ConcreteClass2(Abstract):
    def operation1(self):
        print('Mission 1 accomplished (in a different way).')

    def operation2(self):
        print('Mission 2 accomplished (in a different way).')


if __name__== '__main__':
    c1 = ConcreteClass1()
    c1.template_method()

    print()
    c2 = ConcreteClass2()
    c2.template_method()

