from requests.auth import HTTPProxyAuth
from pymongo import MongoClient
from datetime import datetime
import urllib.request
import requests
import json
import time
import os

def limparConsole():
    Comando = 'clear'
    if os.name in ('nt', 'dos'): Comando = 'cls' # Se o script estiver rodando no Windows.
    os.system(Comando)
Branco = '\033[37m'; Vermelho = '\033[91m'; Verde = '\033[92m'; Amarelo = '\033[93m'; Ciano = '\033[96m'

def Conectado():
    try:
        urllib.request.urlopen('https://google.com', timeout=3)
        return True
    except:
        return False

if Conectado():
    Client = MongoClient('mongodb+srv://Exodus:FelfHdCNF5Onnodg@exodus.hymmlyz.mongodb.net/?retryWrites=true&w=majority')
    Blaze = Client.Blaze
    Recente = Blaze.Recente
    Resultados = Blaze.Resultados

def Resultado():
    Proxy = {'HTTPS': '84.32.32.190:49155'}
    Auth = HTTPProxyAuth('douglasfbfarias', 'LS37hcRjSA')
    blazeAPI = json.loads(requests.get('https://blaze.com/api/roulette_games/recent', proxies=Proxy, auth=Auth).text)
    print(blazeAPI)

Resultado()