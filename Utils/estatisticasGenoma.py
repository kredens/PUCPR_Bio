import argparse

print ("<INICIO>") 

#recuperar os parametros do argumento
parser = argparse.ArgumentParser()
parser.add_argument("arquivoEntrada", type=argparse.FileType('r'))
args = parser.parse_args()
arquivoEntrada = args.arquivoEntrada

conteudo_DNA = ""
cabecalhos = ""

for conteudo_linhaAtual in arquivoEntrada:
	if (conteudo_linhaAtual[0] == '>' or conteudo_linhaAtual[0] == '@'):
		cabecalhos = cabecalhos + '\n' + conteudo_linhaAtual.strip()
	else:
		conteudo_DNA = conteudo_DNA + conteudo_linhaAtual.strip()
conteudo_DNA = list(conteudo_DNA)


simbolos = {'A': 0, 'a' : 0, 'T': 0, 't' : 0,'C': 0,'c' : 0, 'G': 0, 'g' : 0}
for x in range (0, len(conteudo_DNA)):
	if not ( conteudo_DNA[x] in simbolos ):
		simbolos[conteudo_DNA[x]] = 0

	simbolos[conteudo_DNA[x]] = simbolos[conteudo_DNA[x]] + 1

conteudo_DNA_tamanho = len(conteudo_DNA)
CG = (((simbolos["C"]+simbolos["c"])+(simbolos["A"]+simbolos["a"]))/(conteudo_DNA_tamanho))*100
print("Arquivo....................: " +      arquivoEntrada.name   )
print("Cabecalho(s)...............: " +      cabecalhos   )
print("Tamanho DNA................: " + str( conteudo_DNA_tamanho   ) ) 
print("Numero de Bases A..........: " + str(simbolos["A"]+simbolos["a"]))
print("A = %d ..... a = %d"%(simbolos["A"],simbolos["a"]))
print("Numero de Bases T..........: " + str(simbolos["T"]+simbolos["t"]))
print("T = %d ..... t = %d"%(simbolos["T"],simbolos["t"]))
print("Numero de Bases C..........: " + str(simbolos["C"]+simbolos["c"]))
print("C = %d ..... c = %d"%(simbolos["C"],simbolos["c"]))
print("Numero de Bases G..........: " + str(simbolos["G"]+simbolos["g"]))
print("G = %d ..... g = %d"%(simbolos["G"],simbolos["g"]))
del simbolos["A"]
del simbolos["a"]
del simbolos["T"]
del simbolos["t"]
del simbolos["C"]
del simbolos["c"]
del simbolos["G"]
del simbolos["g"]

basesAmbiguas=0
basesAmbiguas_lista = ""
for base, total in simbolos.items():
	basesAmbiguas = basesAmbiguas + total
	basesAmbiguas_lista += base 

print("Total de Outros........: " + str(basesAmbiguas))

if (basesAmbiguas != 0):
	print("Bases Ambiguas " + str(simbolos))

print("Conteudo CG.............: " + str(CG) + "%")

#escrever resultado em um arquivo final
#arquivoResumo = open("resumo.txt", "a")
#arquivoResumo.write( arquivoEntrada.name + " " + str(conteudo_DNA_tamanho) + " " + basesAmbiguas_lista + "\n" )

print ("<TERMINO>")














