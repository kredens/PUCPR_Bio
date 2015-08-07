#RECEBE COMO ENTRADA O NOME DO ARQUIVO, ABRE E DIVIDE EM BLOCOS DE TAMANHO MINIMO E MAXIMO COM DESLOCAMENTO PARA CADA TAMANHO
#ARQUIVO DE SAIDA 1_2.txt - 1- TAMANHO DO BLOCO 2- DESLOCAMENTO
#RETORNA O NUMERO DE ARQUIVOS CRIADOS
def sdb(minSize, maxSize, arquivo):
	import os.path
	import argparse
	from sdb.listConstructor import newlist
	from sdb.VerifTamDoBloco import verificarbloco

	stringNative = ""
	arquivoEntrada = open(arquivo, 'r')

	for conteudo_linhaAtual in arquivoEntrada:
		if conteudo_linhaAtual[0] == '>' :
			conteudo_linhaAtual.strip()	
		else:
			stringNative = stringNative + conteudo_linhaAtual.strip()

	stringNative = list(stringNative.upper())
	address = os.getcwd()
	os.makedirs(address + "/temp/RD")
	control = 0
	number = 0
	for sizeBlock in range (minSize, maxSize+1):
		for startPosition in range (0, sizeBlock):
			control = 0
			posCriar = verificarbloco(sizeBlock,len(stringNative),startPosition)
			if (posCriar == True):
				stringFinal = newlist(sizeBlock, startPosition, stringNative)
				f = open(address+"/temp/RD/"+str(sizeBlock)+"_"+str(startPosition)+".txt", 'w')
				number = number + 1
				for v in range (0, len(stringFinal)):
					f.write(stringFinal[v]+"\t"+str(control)+"\n")
					control = control + len(stringFinal[v])
	return number
