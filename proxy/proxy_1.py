"""
O Proxy  é um padrão de projeto estrutural que tem a intenção
de fornecer um objeto substituto que atua como se fosse um
objeto real que o código cliente gostaria de usar.
O Proxy receberá as solicitações e terá controle sobre quando e
como repassar tais solicitações ao objeto real.

Com base no modo como os proxies são utilizados, nós os classifi-
camos como:

Proxy Virtual: controla acesso a recursos que podem ser caros 
para criação ou utilização.

Proxy Remoto: controla acesso a recursos que estão em servidores
remotos.

Proxy de Proteção: controla acesso a recursos que possam necessitar
autenticação ou permissão.

Proxy Inteligente: além de controlar acesso ao objeto real, também e
executa tarefas adicionais para saber quando e como executar
determinadas ações.


Proxys podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços, criar cache,
criar ou destruir objetos, adiar execuções e muito mais...
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict

class IUser(ABC):
    """ Subject Interface """
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self)-> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self)-> Dict: pass


class RealUser():
    """ Real Subject """
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2) # Simulando requisição
        self.firstname = firstname
        self.lastname = lastname
    
    def get_addresses(self)-> List[Dict]:
        sleep(2) # Simulando requisição
        return[
            {'Av': 'Brasil', 'Nº': 500}
        ]

    def get_all_user_data(self)-> Dict:
        sleep(2) # Simulando requisição
        return{
            'CPF': '111.111.111-11',
            'RG': '111.111.11-1'
        }
        

class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self._real_user: RealUser

        self._cached_adresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self)-> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)
        
    def get_addresses(self)-> List[Dict]:
        self.get_real_user()
        if not hasattr(self, '_cached_adresses'):
            self._cached_adresses = self._real_user.get_addresses()

        return self._cached_adresses
    
    def get_all_user_data(self)-> Dict:
        self.get_real_user()
        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data

if __name__ == '__main__':
    pedro = UserProxy('Pedro', 'Luiz e a Parede')

    print(pedro.firstname)
    print(pedro.lastname)

    # 6 segundos:
    print(pedro.get_all_user_data())
    print(pedro.get_addresses())


    # Responde instantaneamente:
    print('Cached DATA:')
    for i in range(50):
        print(pedro.get_addresses())
    


