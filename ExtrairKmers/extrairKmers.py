print ("<INICIO>") 
import math
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.palavras_database

# Config
cfg_tamanhoPalavra = 10

arquivoEntrada = open('NC_017651.1.fasta', 'r')

jahPegouPrimeiraLinha = False
conteudo_DNA = ""

for conteudo_linhaAtual in arquivoEntrada:
	if not jahPegouPrimeiraLinha:
		jahPegouPrimeiraLinha = True
		conteudo_primeiraLinha = conteudo_linhaAtual.strip()
	else:
		conteudo_DNA = conteudo_DNA + conteudo_linhaAtual.strip()

#conteudo_DNA = "abcdefghijklmnopqrstuvxzwyKABC"
#1   2   3   4   5   6   7   8  
#abc def ghi jkl mno pqr stu vxz wy

conteudo_DNA_tamanho = len(conteudo_DNA)
#print("cfg_tamanhoPalavra......: " + str( cfg_tamanhoPalavra     ) )
#print("Cabecalho...............: " +      conteudo_primeiraLinha   )
#print("Tamanho DNA.............: " + str( conteudo_DNA_tamanho   ) ) 
#print("DNA.....................: " +      conteudo_DNA             )

palavras = db.palavras

for deslocamentoAtual in range(0, cfg_tamanhoPalavra):
	conteudo_DNA_tamanho = len(conteudo_DNA) - deslocamentoAtual
	quantidadeDePalavras = math.floor(conteudo_DNA_tamanho / cfg_tamanhoPalavra)

	#print("\n 	deslocamentoAtual.......: " + str( deslocamentoAtual))
	#print("		Tamanho DNA.............: " + str( conteudo_DNA_tamanho)) 
	#print("		Quantidade de Palavras..: " + str( quantidadeDePalavras   ) )

	posicaoAtual = deslocamentoAtual
	posicaoFinal = cfg_tamanhoPalavra + deslocamentoAtual
	for palavraAtual in range(0, quantidadeDePalavras):
		conteudo_palavraAtual = conteudo_DNA[posicaoAtual:posicaoFinal]
		#print("			palavraAtual...:" + str(palavraAtual))
		#print(" 		txt............:" + conteudo_palavraAtual)

		posicaoAtual = posicaoFinal
		posicaoFinal = posicaoFinal + cfg_tamanhoPalavra

		palavra = {"tamanhoPalavra"    : cfg_tamanhoPalavra,
		           "deslocamentoAtual" : deslocamentoAtual,
		           "palavra"           : conteudo_palavraAtual,
		           "palavraAtual"      : palavraAtual,
		           "posicaoInicio"     : posicaoAtual,
		           "posicaoFim"        : posicaoFinal}

		palavras.insert_one(palavra)

print ("<TERMINO>")







