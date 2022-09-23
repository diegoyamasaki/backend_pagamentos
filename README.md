# Backend de Pagamentos

Backend desenvolvido como parte do teste para a will bank. Foi utlizado sqlite como banco para persistencia pois
nesse inicio de desenvolvimento o banckend não fica preso a um tipo especifico de banco e com sqlite agiliza o
desenvolviemnto inicial.

Para essa aplicação foi utilizado também  rabbitmq como mensageria para as notificações que falharem assimp poderem ser
reenviadas novamente assim que o sistema de notificação estiver estabelecido novamente.

Para facilitar os testes e visualizar a aplicação foi criado um docker compose (https://docs.docker.com/compose/)

A aplicação foi desenvolvida em python e utilizando o framework fastapi (https://fastapi.tiangolo.com/), como ORM
para o banco de dados foi utilizado o SQLAlchemy (https://www.sqlalchemy.org/)

A aplicação tem 2 tipos de documentações geradas automaticamente pelo framework utlizado

- Swagger (https://swagger.io/) -> http://localhost:8000/docs
- Redoc (https://github.com/Redocly/redoc) -> http://localhost:8000/redoc


## Mock de requisição do serivço de notificação de pagamento
https://run.mocky.io/v3/0bca48f0-16db-4726-96a8-d4206306f698


## Iniciando docker compose
```commandline
# Comando para iniciar o docker compose
$ docker compose up
```

## Parando docker compose
```commandline
# Comando para iniciar o docker compose
$ docker compose down
```


Qualquer duvidas por favor entrar em contato: yamasaki.diego@gmail.com

Obrigado!
