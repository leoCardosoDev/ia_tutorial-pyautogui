import requests
from bs4 import BeautifulSoup
import pandas as pd

def scraping_uf(uf: str):
    uf_url = f"https://www.ibge.gov.br/cidades-e-estados/{uf}.html"
    browsers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(uf_url, headers=browsers)
    if response.status_code != 200:
        raise Exception(f"Failed to load page: {uf_url}")
    soup = BeautifulSoup(response.content, 'html.parser')
    indicadores = soup.select('.indicador')
    uf_dict = {
        dado.select('.ind-label')[0].text: dado.select('.ind-value')[0].text
        for dado in indicadores
    }
    return uf_dict

estado = scraping_uf('sp')

for indicador in estado:
    if ']' in estado[indicador]:
        estado[indicador] = estado[indicador].split(']')[0][:-8]
    else:
        estado[indicador] = estado[indicador]


df = pd.DataFrame(estado.values(), index=estado.keys())
print(df)
