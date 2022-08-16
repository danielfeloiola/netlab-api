## NETLAB API

Uma API que recebe as medidas de pétalas e sépalas e responde com o tipo de iris

# Tecnologias

- FastAPI
- Uvicorn
- Sentry

# Instalação

Para utilizar com o uvicorn siga os seguintes passos:

- Crie um virtualenv do Python
- Baixe o repositório e entre no diretório
- Instale as dependências necessárias com ```pip install -r requirements.txt```
- (opcional) Se quiser utilizar o Sentry para acessar os logs, crie uma variável de ambiente com o DSN usando um código como ```export SENTRY_DSN=me-troque-pela-sua-dsn```
- Execute o uvicorn para iniciar o servidor: ```uvicorn app.main:app —-reload```

Para utilizar com o Docker:

- Crie um virtualenv do Python
- Baixe o repositório e entre no diretório
- Cria uma imagem do Docker: ```docker build -t netlab-api .```
- Execute o programa: ```docker run -d --name netlab-api-container -p 80:80 netlab-api```

Para utilizar o Sentry com o Docker é necessário utilizar a flag ```-e``` ao executar: ```-e SENTRY_DSN=me-troque-pela-sua-dsn```

# Utilizando a API:

Para acessar a página com a documentação da FastAPI, é necessário usar um navegador e acessar a URL
- No caso de estar usando o uvicorn: ```127.0.0.1:8000/docs```
- No caso do Docker container: ```0.0.0.0/docs```

No endpoint /classifier o botão "try it out" permite inserir os 4 valores (em formato float) e ver a resposta enviada pelo servidor.

Também é possível utilizar um programa como o Insomnia para testar o envio de requisições, utilizando sempre o método GET e a endpoint /classifier.
No caso de um Docker container, por exemplo, uma requisição para 
```http://0.0.0.0/classifier?sepal_lenght=7.1&sepal_width=6.4&petal_lenght=5.5&petal_width=2.3``` irá retornar o objeto ```{"species": "virginica"}```

Os logs ficam no arquivo logs.log dentro da pasta /app
Para acessar os logs no Sentry, é necessário criar uma conta no site (sentry.io) e obter uma DSN para o envio dos logs