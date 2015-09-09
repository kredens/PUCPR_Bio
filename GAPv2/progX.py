import os.path
import argparse
import shutil #Deletar pastas
from os import rename

#PARAMETERS NAME OF THE FILE, MINIMUM BLOCK SIZE AND MAXIMUM BLOCK SIZE
parser = argparse.ArgumentParser()
parser.add_argument("nomeArquivoFasta", type=str)
parser.add_argument("minbloco", type=int)
parser.add_argument("maxbloco", type=int)
args = parser.parse_args()
arquivoAtual = args.nomeArquivoFasta
minbloco = args.minbloco
maxbloco = args.maxbloco

if(minbloco>maxbloco or minbloco <= 0):
	print("Invalid Block Size")
else:
	#CREATING THE DIRS(IF IT DOESNT EXIST)
	address = os.getcwd()
	if (os.path.exists(address + "/BLOCKS") == True):
		shutil.rmtree(address + "/BLOCKS")
	os.makedirs(address + "/BLOCKS")
	#CALLING THE FUNCTION TO CREAT THE BLOCKS
	#SIZE OF THE BLOCO
	for tamanhoBlocoAtual in range(minbloco, maxbloco+1):
		os.system("grep -v '>' "+arquivoAtual+" | awk -v block="+str(tamanhoBlocoAtual)+" -f BreakGenome.awk > "+"BLOCKS/G_"+str(tamanhoBlocoAtual)+".txt")
		#RENAMEING MEANING THE FILE IS READY
		rename("BLOCKS/G_"+str(tamanhoBlocoAtual)+".txt", "BLOCKS/R_"+str(tamanhoBlocoAtual)+".txt")	
