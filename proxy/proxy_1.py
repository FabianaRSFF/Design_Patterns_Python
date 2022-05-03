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



