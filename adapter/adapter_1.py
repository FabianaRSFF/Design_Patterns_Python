"""
Padrão de projeto estrutural que tem a intenção de permitir que
duas classes que seriam incompatíveis trabalhem em conjunto 
através de um 'adaptador'.U+1F446	U+1F449	U+1F447	U+1F448
"""
from abc import ABC, abstractmethod

class IControl(ABC):
    @abstractmethod
    def top(self)-> None: pass

    @abstractmethod
    def right(self)-> None: pass

    @abstractmethod
    def down(self)-> None: pass

    @abstractmethod
    def left(self)-> None: pass


class Control(IControl):
    def top(self)-> None:
        print('Movendo para cima...\U0001F446')

    def right(self)-> None:
        print('Movendo para a direita...\U0001F449')

    def down(self)-> None:
        print('Movendo para baixo...\U0001F447')

    def left(self)-> None:
        print('Movendo para a esquerda...\U0001F448')


class NewControl:
    def move_top(self)-> None:
        print('New control: Movendo para cima...\U0001F446')

    def move_right(self)-> None:
        print('New control: Movendo para a direita...\U0001F449')

    def move_down(self)-> None:
        print('New control: Movendo para baixo...\U0001F447')

    def move_left(self)-> None:
        print('New control: Movendo para a esquerda...\U0001F448')


class ControlAdapter:
    """ Adapter Object """
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self)-> None:
        self.new_control.move_top()

    def right(self)-> None:
        self.new_control.move_right()

    def down(self)-> None:
        self.new_control.move_down()

    def left(self)-> None:
        self.new_control.move_left()


class ControlAdapter2(Control, NewControl):
    """ Adapter Class """
    def top(self)-> None:
        self.move_top()

    def right(self)-> None:
        self.move_right()

    def down(self)-> None:
        self.move_down()

    def left(self)-> None:
        self.move_left()


if __name__ == '__main__':
    """ Control Adapter Object"""
    c1 = Control()
    new_control = NewControl()
    control_object = ControlAdapter(new_control)
    
    c1.top()
    c1.right()
    c1.down()
    c1.left()

    print()

    control_object.top()
    control_object.right()
    control_object.down()
    control_object.left()

    print()

    """ Control Adapter Class """
    control_class = ControlAdapter2()
    control_class.top()
    control_class.left()
    control_class.right()
    control_class.down()