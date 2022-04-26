# Monostate ou Borg - É uma variação do singleton para 
# garantir que
# estado do objeto seja igual para todas as instâncias.

class A:
    def __init__(self, nome):
        self.x = 10
        self.y = 20
        self.nome = nome

    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

a = A('Luiz')
print(a)
