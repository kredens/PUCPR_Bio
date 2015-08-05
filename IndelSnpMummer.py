import argparse

def check(a, b):
	if (a == "."):
		return "insertion"
	else:
		if (b == "."):
			return "deletion"
		else:
			return "mutation"


parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
arquivo = args.filename
arquivoEntrada = open(arquivo, 'r')

ultimaPosicao = 0
flag = False
delsize = {1 : 0, 2: 0, 3 : 0}
blocodel = 0
insertsize = {1: 0, 2: 0, 3 : 0}
blocoinsert = 0
mutsize = {1 : 0, 2: 0, 3 : 0}
blocomut = 0
bloco = False
size = 0
insert = 0
delet = 0
mutat = 0
lastanswer = ""
for conteudo_linhaAtual in arquivoEntrada:
	if (flag == True):
		#Avaliando a linha atual
		stringlist = conteudo_linhaAtual.split()
		resposta = check(stringlist[1], stringlist[2])
		posicao = int(stringlist[0])
		#Somando os blocos (snp ou indels seguidos)
		if (posicao == ultimaPosicao + 1):
			if (bloco == True): #Meio do bloco
				size = size + 1
			else: #Inicio de Bloco
				bloco = True
				size = 2
		else:
			if (bloco == True): #Fim de bloco
				bloco = False
				if (lastanswer == "insertion"):
					if not (size in insertsize):
						insertsize[size] = 0
					insertsize[size] = insertsize[size] + 1
					blocoinsert = blocoinsert + 1
					size = 0
				if (lastanswer == "deletion"):
					if not (size in delsize):
						delsize[size] = 0
					delsize[size] = delsize[size] + 1
					blocodel = blocodel + 1
					size = 0
				if (lastanswer == "mutation"):
					if not (size in delsize):
						mutsize[size] = 0
					delsize[size] = delsize[size] + 1
					blocomut = blocomut + 1
					size = 0
		#Somando os totais
		if (resposta == "insertion"):
			insert = insert + 1
		if (resposta == "deletion"):
			delet = delet + 1
		if (resposta == "mutation"):
			mutat = mutat + 1
		#Preparando para proxima rodada
		lastanswer = resposta
		ultimaPosicao = int(stringlist[0])
	#Tirando o cabecario
	if (conteudo_linhaAtual[0] == "="):
		flag = True
		
#Preenchendo os blocos de tamanho 1
delsize["1"] = delet - blocodel
insertsize["1"] = insert - blocoinsert
mutsize["1"] = mutat - blocomut

#Imprimindo os resultados
print("\n\n")
print("******RESULTS******")
print("Total Mutation (Numb of bases)....: " + str(mutat))
print("Mutations: (Size: NumberOf)"+str(mutsize))
print("Total Insertions (Numb of bases)....: " + str(insert))
print("Insertions: (Size: NumberOf)"+str(insertsize))
print("Total Deletions (Numb of bases).....: " + str(delet))
print("Deletions:  (Size: NumberOf)"+str(delsize))
print("\n\n")
