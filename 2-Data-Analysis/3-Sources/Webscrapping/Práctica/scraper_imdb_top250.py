from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import json
from fake_useragent import UserAgent

url = "https://www.imdb.com/chart/top/"
ua = UserAgent()
headers = {'User-Agent': ua.random}
response = requests.get(url, headers=headers)
soup = bs(response.content, 'html.parser')

dict_peliculas_250 = {"Ranking": [x['currentRank'] for x in json.loads(soup.find("script", id="__NEXT_DATA__").get_text())['props']['pageProps']['pageData']['chartTitles']['edges']],
                      "Titulo": [x['item'].get("alternateName", x['item'].get("name")) for x in json.loads(soup.find("script", type="application/ld+json").get_text())['itemListElement']],
                      "Año": [x['node']['releaseYear']['year'] for x in json.loads(soup.find("script", id="__NEXT_DATA__").get_text())['props']['pageProps']['pageData']['chartTitles']['edges']],
                      "Duración": [x['item']['duration'][2:] for x in json.loads(soup.find("script", type="application/ld+json").get_text())['itemListElement']],
                      "Rating": [x['item']['aggregateRating']['ratingValue'] for x in json.loads(soup.find("script", type="application/ld+json").get_text())['itemListElement']]}
df = pd.DataFrame(dict_peliculas_250)
df.to_csv("top250.csv")