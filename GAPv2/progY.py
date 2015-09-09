import os.path
import argparse
import shutil #Deletar pastas
import numpy #http://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html

#MINIMUM BLOCK SIZE, MAXIMUM BLOCK SIZE AND MAX COEFFICIENT OF VARIATION
parser = argparse.ArgumentParser()
parser.add_argument("minbloco", type=int)
parser.add_argument("maxbloco", type=int)
#parser.add_argument("desvMax", type=int)
args = parser.parse_args()
minbloco = args.minbloco
maxbloco = args.maxbloco
numberImportantWords = 15
#desvMax = args.desvMax
address = os.getcwd()

#ANALYSING THE FILES THAT ARE READY IN THE BLOCKS DIR
filesAnalised = 0;
target = minbloco
while(filesAnalised < (maxbloco-minbloco+1)):
	targetfile = ("BLOCKS/R_"+str(target)+".txt")
	if(os.path.isfile(address+"/"+targetfile)==True):
		if (os.path.exists(address + "/TEMPS") == False):
			os.makedirs(address + "/TEMPS")
		#currentFile = open(address+"/"+targetfile, 'r')
		os.system("cut "+targetfile+" -d' ' -f 1 | sort | uniq -c -d | sort -g | tail -n "+str(numberImportantWords)+" > TEMPS/M_"+targetfile[9:])
		MostUsedWords = open(address+"/TEMPS/M_"+targetfile[9:])
		ListWords = []
		for Line in MostUsedWords:
			posicao = Line.rfind(" ")
			ListWords.append(Line[posicao+1:-1])
		MostUsedWords.close()
		#os.remove("TEMPS/M_"+targetfile[9:])
		for control in range(0,len(ListWords)):
			word = ListWords[control]
			os.system("grep "+word+" "+targetfile+" > TEMPS/W_"+targetfile[9:]+"_"+str(control))
		for control in range(0, len(ListWords)):
			listPosition = []
			listFinal = []
			AnalisingFile = open(address+"/TEMPS/W_"+targetfile[9:]+"_"+str(control))
			for x in AnalisingFile:
				posicao = x.find(" ")
				word = x[:posicao]
				posicao = x.rfind(" ")
				listPosition.append(int(x[posicao+1:-1]))
			AnalisingFile.close()
			for x in range(1, len(listPosition)):
				listFinal.append(listPosition[x]-listPosition[x-1])
			CofVarietion = (numpy.std(listFinal)/numpy.mean(listFinal))
			print(word)
			print(CofVarietion)

		target = target + 1
		filesAnalised = filesAnalised +1
