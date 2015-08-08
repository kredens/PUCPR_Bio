import os.path
import argparse
import shutil #Deletar pastas
import numpy
from tools.sdb.sdbmain import sdb
from tools.funcoesshell import nameAllfiles
from tools.funcoesshell import palavrasPrincipais
from tools.funcoesshell import achaPosicaoPalavraNoTexto
from subprocess import call

#Adicionando os parametros de entrada: tamanho minimo e maximo dos blocos
parser = argparse.ArgumentParser()
parser.add_argument("minblock", type=int)
parser.add_argument("maxblock", type=int)
parser.add_argument("desviomax", type=int)
args = parser.parse_args()
minblock = args.minblock
maxblock = args.maxblock
desviomax = args.desviomax
#Excluindo pastas TEMP e RESULTS caso elas existam
'''
ESCREVER CODIGO PARA EXCLUIR PASTA TEMP E RESULTS CASO EXISTAM
'''
#Localizando o endereco atual
address = os.getcwd()
os.makedirs(address + "/temp")
os.makedirs(address + "/RESULTS")
#CriandoPastacomResultados
if(minblock <= maxblock and minblock > 0):
	#Descobrindo o numero de arquivos de genomas
	print(address+"/ENTERFILES")
	numArquivosEntrada = nameAllfiles(address, "ENTERFILES", "allFilesName")
	#Iniciando o processamento para cada um dos arquivos
	if (numArquivosEntrada != 0):
		allFilesName = open(address + "/temp/allFilesName.txt")
		relatorioPrincipal = open(address+"/RESULTS/MainResults.txt", 'w')
		relatorioPrincipal.write("MAIN RESULTS:\n")
		for arquivoAtual in allFilesName:
			print("Arquivo sendo processado:"+arquivoAtual)
			#Criando Arquivo de Resultado para Este Genoma
			f = open(address+"/RESULTS/"+"R_"+arquivoAtual+".txt", 'w')
			f.write("RESULTADOS DO ARQUIVOS: "+arquivoAtual+"\n"+"*"*10+"\n")
			#Separando em blocos dos tamanhos minimo e maximo
			numArquivosBlocos = sdb(minblock,maxblock,"ENTERFILES/"+arquivoAtual[:-1])
			#Descobrindo o nome dos arquivos com blocos
			nameAllfiles(address, "temp/RD", "allBlocksFiles")
			allBlocksFiles = open(address + "/temp/allBlocksFiles.txt")
			for arquivoBlocoAtual in allBlocksFiles:
				#Descobrindo as palavras Principais
				padlavrasPrincipais(arquivoBlocoAtual, address)
				listaPalavras = open(address + "/temp/MostUsedWords/"+arquivoBlocoAtual+".txt")
				for palavraAtual in listaPalavras:
					#Achando as ocorrencias da palavra
					listaPosicoes = achaPosicaoPalavraNoTexto(palavraAtual[:-1], arquivoBlocoAtual, address)
					numeroDeVezesQueAparece = len(listaPosicoes)
					#Caso tenha aparecido apenas uma ou duas vezes nao ha como calcular o desvio padrao
					if (numeroDeVezesQueAparece > 2):
						devPadrao = numpy.std(listaPosicoes)
						f.write("***Block (Size/Deplacement): "+arquivoBlocoAtual+", Genome Block: "+palavraAtual+", Std Deviation: "+str(devPadrao)+"\n")
						if (devPadrao <= desviomax):
							relatorioPrincipal.write("***Genome: "+arquivoAtual+". Block (Size/Deplacement): "+arquivoBlocoAtual+", Genome Block: "+palavraAtual+", Std Deviation: "+str(devPadrao)+"\n")
					f.write("\n"+"*"*3+"\n")
			shutil.rmtree(address + "/temp/RD")	


	else:
		print("ERRO FINDING THE ENTERFILES, BE SURE ALL FILES IN THE ENTERFILES DIRC ARE GENOME FASTA FILES")
else:
	print("THE MINIMUM SIZE MUST BE, AT LEST AS BIG AS THE MAXIMUM SIZE, AND IT CANNOT BE IQUAL TO 0")
