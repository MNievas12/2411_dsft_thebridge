from fastapi import FastAPI, HTTPException
import pickle
import uvicorn
# from pydantic import BaseModel
import sqlite3
import pandas as pd

app = FastAPI()


# class InputData(BaseModel):
#     tv: int
#     radio: int
#     newspaper: int


@app.get("/")
async def hello():
    return {"message": "Bienvenido a mi API del modelo de Advertising"}

# 1. Endpoint de predicción
@app.post("/predict")
async def predict(input:dict):
    model = pickle.load(open("data/advertising_model.pkl", 'rb'))
    data = input.get("data")
    if not data:
        raise HTTPException(status_code=400, detail="No se han proporcionado datos")
    try:
        prediction = model.predict(data)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al realizar la predicción. ")


# 2. Endpoint de ingesta de datos
@app.post("/ingest")
async def ingest(input:dict):
    data = input.get("data")
    if not data:
        raise HTTPException(status_code=400, detail="No se han proporcionado datos")
    try:
        conn = sqlite3.connect('./data/advertising.db')
        cursor = conn.cursor()
        query = """INSERT INTO campañas VALUES (?,?,?,?)"""
        for fila in data:
            cursor.execute(query, fila)
        conn.commit()
        conn.close()
        return {"message": 'Datos ingresados correctamente'}
    except Exception as e:
            raise HTTPException(status_code=500, detail="Error al ingestar los datos. ")

# 3. Endpoint de reentramiento del modelo
@app.post("/retrain")
async def retrain():
    try:
        conn = sqlite3.connect('./data/advertising.db')
        cursor = conn.cursor()
        query = "SELECT * FROM campañas"
        result = cursor.execute(query)
        df = pd.DataFrame(result)
        conn.close()
        model = pickle.load(open("data/advertising_model.pkl", 'rb'))
        model.fit(df.iloc[:,:-1], df.iloc[:,-1])
        pickle.dump(model, open('./data/advertising_model.pkl', 'wb'))
        return {'message': 'Modelo reentrenado correctamente.'}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al reentrenar el modelo. ")


# uvicorn.run(app)
