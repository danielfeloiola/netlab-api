from fastapi import FastAPI, Request
from .logger import logger
import pandas as pd
import joblib

# cria o app
app = FastAPI()

# Carrega o classificador
with open('app/iris_classifier.joblib', 'rb') as f:
    iris_classifier = joblib.load(f)


@app.get('/classifier')
async def root(sepal_lenght: float,sepal_width: float, petal_lenght: float, petal_width: float, request: Request):
    '''
    Recebe os 4 parametros em formato de float e classifica a flor
    Os valores são passados como parametros na url
    '''

    # coloca a chamada no log
    logger.info(f'CHAMADA url={request.url}')

    # cria uma flor...
    flower = {}
    flower['sepal_lenght'] = sepal_lenght
    flower['sepal_width'] = sepal_width
    flower['petal_lenght'] = petal_lenght
    flower['petal_width'] = petal_width

    # faz a classificacao e responde
    flower = pd.DataFrame([flower])
    species = iris_classifier.predict(flower)

    logger.info(f'RESPOSTA: { str({"species": species[0]})}' )
   
    return {"species": species[0]}

