print ("<INICIO>") 
import math
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.palavras_database



# para cada DESLOCAMENTO
deslocamentos = db.palavras.distinct( "deslocamentoAtual" )
for deslocamento in deslocamentos:
	print("Deslocamento..: " + str(deslocamento))

	#recuperar kmers com aparição maior que 2
	kmers = db.palavras.find()


#palavras = db.palavras.find()
#for palavra in palavras:
#    print(palavra)

#calcular DP para cada kmer


print ("<TERMINO>") 