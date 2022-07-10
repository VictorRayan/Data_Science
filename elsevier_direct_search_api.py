import requests
from pandas import read_csv

api_key = ""

#database  = read_csv('./dependencies/magnetic-dimensionality-v100.csv')
search_word1 = input("informe o primeiro termo a ser buscado: ")
search_word2 = input("informe o segundo termo a ser buscado: ")
qnt_return = input("informe a quantidade de resultados a serem retornados: ")

def search_elsevier(word_search, qnt): 
    response = requests.get("https://api.elsevier.com/content/search/scopus?query="+word_search+"&count="+str(qnt)+"&httpAccept=application/json&apiKey="+api_key)
    return response.content


print (search_elsevier(search_word1+" "+search_word2, qnt_return))



