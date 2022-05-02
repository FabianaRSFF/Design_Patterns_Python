"""
Chain of responsability:
Padrão comportamental que tem a intenção de evitar o 
acoplamento do remetente de uma solicitação ao seu receptor, 
ao dar a mais de um objeto a oportunidade de tratar a soli-
citação. Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""

# Implementando com funções:


def handler_ABC(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f'handler_ABC, conseguiu tratar o valor {letter}.'
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter in letters:
        return f'handler_DEF, conseguiu tratar o valor {letter}.'
    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    return f'handler_unsolved: não sei tratar  {letter}.'


if __name__ == '__main__':
    print(handler_ABC('A'))
    print(handler_ABC('B'))
    print(handler_ABC('C'))
    print(handler_ABC('D'))
    print(handler_ABC('Z'))
    print("\U0001F60A")
    print("\U0001F496")
    print("\U00002763")

"""
De todos os padrões de projeto comportamentais, 
meus preferidos foram os template_methods e o
chain of responsability.U+1F60A		U+2763	U+1F496	
"""
