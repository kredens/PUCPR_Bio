#Funcao que recebe o nome do arquivo e busca as 10 palavras principais (mais repetidas) deste arquivo
#Cria como saida um texto com o a palavra e o numero de vezes em que esta palavra apareceu
def palavrasPrincipais (ArquivoEntrada, address):
	import os.path
	os.makedirs(address + "temp/MostUsedWords", "-p")
	try:
		os.system("cut -f 1 RD/"+ArquivoEntrada+".txt | sort | uniq -c | sort -g | tail > temp/MostUsedWords/"+ArquivoEntrada+".txt")
	except:
		return False
	return True

#Recebe o endereco e cria um arquivo na pasta temp como o nome de todos os arquivos dentro da pasta ENTERFILES
#address = Endereco do Main
#TargetDir = diretorio alvo (sem / no inicio e no final)
def nameAllfiles (address, TargetDir, exitname):
	import os.path
	numberoArq = 0
	try:
		os.system("ls "+TargetDir+" -lit > temp/allfilesterminal.txt")
		newfile = open(address+"/temp/"+exitname+".txt", "w")
		arquivoEntrada = open(address+"/temp/allfilesterminal.txt", 'r')
	except:
		return 0
	for conteudo_linhaAtual in arquivoEntrada:
		if (conteudo_linhaAtual[0] == "t"):
			conteudo_linhaAtual.strip()
		else:
			numberoArq = numberoArq + 1
			posicao = conteudo_linhaAtual.rfind(" ")
			newfile.write(conteudo_linhaAtual[posicao+1:])
			conteudo_linhaAtual.strip()
	os.remove(address+"/temp/allfilesterminal.txt")
	return numberoArq

#Localiza as palavras de um texto e retorna uma lista com a posicao de cada palavra
def achaPosicaoPalavraNoTexto (palavra, arquivoTarget ,address):
	try:
		os.system("grep "+palavra+" RD/"+arquivoTarget+" > temp/posicao.txt")
		arquivoEntrada = open(address+"/temp/posicao.txt", 'r')
	except:
		return False
	positionList = []
	for conteudo_linhaAtual in arquivoEntrada:
		posicao = conteudo_linhaAtual.rfind("\t")
		positionList.append(conteudo_linhaAtual[posicao+1:])
		conteudo_linhaAtual.strip()
	os.remove(address+"/temp/posicao.txt")
	return positionList
