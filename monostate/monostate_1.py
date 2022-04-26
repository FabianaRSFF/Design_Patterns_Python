# Monostate ou Borg - É uma variação do singleton para 
# garantir que
# estado do objeto seja igual para todas as instâncias.
from pip import main


class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state = {
        'x': 10,
        'y': 20,
    }

    def __init__(self):
        self.x = 1
        self.__dict__ = self._state

if __name__ == '__main__':
    m1 = MonoStateSimple()
    m2 = MonoStateSimple()
    print(m1)
    print(m2)
    # Se  você muda o valor em uma classe, o valor muda nas duas.
    m1.x = 'qualquer coisa'
    print(m1)
    print(m2)