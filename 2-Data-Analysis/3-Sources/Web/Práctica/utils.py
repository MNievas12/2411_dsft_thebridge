import hashlib
import requests
import datetime
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

def hash_params(timestamp,priv_key,pub_key):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

def obtener_personajes(url, params):
    res = requests.get(url,params=params)
    return res.json()

def almacenar_dataframe(res):
    marvel_dict = {"id": [x.get("id") for x in res['data']['results']],
               "name": [x.get("name") for x in res['data']['results']],
               "picture_url": [x.get("thumbnail").get("path") + "." + x.get("thumbnail").get("extension") for x in res['data']['results']]}
    return pd.DataFrame(marvel_dict)

def guardar_personajes(nombre):
    params = {'ts': timestamp, 
            'apikey': os.getenv('pub_key'), 
            'hash': hash_params(timestamp,os.getenv('priv_key'),os.getenv('pub_key')),
            'nameStartsWith': nombre[0],
            'offset': 0,
            'limit': 100
            };

    url = 'http://gateway.marvel.com/v1/public/characters'

    res = obtener_personajes(url, params)

    df = almacenar_dataframe(res)

    while len(df) < res['data']['total']:
        print("Aún faltan datos por obtener")
        params['offset'] += 100
        res = obtener_personajes(url, params)
        df = pd.concat([df, almacenar_dataframe(res)])

    df.to_csv("./data/marvel_" + nombre[0] + ".csv")