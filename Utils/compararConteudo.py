import argparse

#recuperar os parametros do argumento
parser = argparse.ArgumentParser()
parser.add_argument("arquivo1", type=argparse.FileType('r'))
parser.add_argument("arquivo2", type=argparse.FileType('r'))
args = parser.parse_args()
arquivo1 = args.arquivo1
arquivo2 = args.arquivo2

dna1_conteudo = ""
dna1_cabecalho = ""
dna1_alfabeto = {'A': 0, 'a' : 0, 'T': 0, 't' : 0,'C': 0,'c' : 0, 'G': 0, 'g' : 0}

dna2_conteudo = ""
dna2_cabecalho = ""
dna2_alfabeto = {'A': 0, 'a' : 0, 'T': 0, 't' : 0,'C': 0,'c' : 0, 'G': 0, 'g' : 0}

os_dnas_sao_iguais = True

#carregar DNA 1
for tmp_linhaAtual in arquivo1:
	if (tmp_linhaAtual[0] == '>' or tmp_linhaAtual[0] == '@'):
		dna1_cabecalho = dna1_cabecalho + '\n' + tmp_linhaAtual.strip()
	else:
		dna1_conteudo = dna1_conteudo + tmp_linhaAtual.strip()

#carregar DNA 2
for tmp_linhaAtual in arquivo2:
	if (tmp_linhaAtual[0] == '>' or tmp_linhaAtual[0] == '@'):
		dna2_cabecalho = dna2_cabecalho + '\n' + tmp_linhaAtual.strip()
	else:
		dna2_conteudo = dna2_conteudo + tmp_linhaAtual.strip()

#percorrer DNA 1
for x in range(0, len(dna1_conteudo)):
	#verificar se tem base diferente
	if( dna1_conteudo[x] != dna2_conteudo[x] ):
		os_dnas_sao_iguais = False

	#verificar se é um simbolo não previsto no alfabeto
	if not ( dna1_conteudo[x] in dna1_alfabeto ):
		dna1_alfabeto[dna1_conteudo[x]] = 0

	#contabilizar o total de vezes que o simbolo aparece
	dna1_alfabeto[dna1_conteudo[x]] = dna1_alfabeto[dna1_conteudo[x]] + 1

#percorrer DNA 2
#esse for serve somente para computar a distribuição de bases do DNA 2
for z in range (0, len(dna2_conteudo)):
	if not ( dna2_conteudo[z] in dna2_alfabeto ):
		dna2_alfabeto[dna2_conteudo[z]] = 0

	dna2_alfabeto[dna2_conteudo[z]] = dna2_alfabeto[dna2_conteudo[z]] + 1


#print("Arquivo 1....................: " +      arquivo1.name   )
#print("Cabecalho(s)...............: " +      dna1_cabecalho   )
#print("Arquivo 2....................: " +      arquivo2.name   )
#print("Cabecalho(s)...............: " +      dna2_cabecalho   )
print("São iguais?........................: " + str(os_dnas_sao_iguais))
print ("+----------+-----------------------------------+-----------------------------------+-----------------------------------+")
print ("|          |               DNA 1               |               DNA 2               |             Diferença             |")
print ("|----------+-----------------------------------+-----------------------------------+-----------------------------------+")
print ("|        A |" + str(dna1_alfabeto["A"]).center(35) + "|"  + str(dna2_alfabeto["A"]).center(35) + "|" + str(dna1_alfabeto["A"] - dna2_alfabeto["A"]).center(35) + "|" )
print ("|----------+-----------------------------------+-----------------------------------+-----------------------------------+")
print ("|        a |" + str(dna1_alfabeto["a"]).center(35) + "|"  + str(dna2_alfabeto["a"]).center(35) + "|" + str(dna1_alfabeto["a"] - dna2_alfabeto["a"]).center(35) + "|" )
print ("|----------+-----------------------------------+-----------------------------------+-----------------------------------+")
print ("|        T |" + str(dna1_alfabeto["T"]).center(35) + "|"  + str(dna2_alfabeto["T"]).center(35) + "|" + str(dna1_alfabeto["T"] - dna2_alfabeto["T"]).center(35) + "|" )
print ("|----------+-----------------------------------+-----------------------------------+-----------------------------------+")
print ("|        t |" + str(dna1_alfabeto["t"]).center(35) + "|"  + str(dna2_alfabeto["t"]).center(35) + "|" + str(dna1_alfabeto["t"] - dna2_alfabeto["t"]).center(35) + "|" )
print ("|----------+-----------------------------------+-----------------------------------+-----------------------------------+")
print ("|        C |" + str(dna1_alfabeto["C"]).center(35) + "|"  + str(dna2_alfabeto["C"]).center(35) + "|" + str(dna1_alfabeto["C"] - dna2_alfabeto["C"]).center(35) + "|" )
print ("|----------+-----------------------------------+-----------------------------------+-----------------------------------+")
print ("|        c |" + str(dna1_alfabeto["c"]).center(35) + "|"  + str(dna2_alfabeto["c"]).center(35) + "|" + str(dna1_alfabeto["c"] - dna2_alfabeto["c"]).center(35) + "|" )
print ("|----------+-----------------------------------+-----------------------------------+-----------------------------------+")
print ("|        G |" + str(dna1_alfabeto["G"]).center(35) + "|"  + str(dna2_alfabeto["G"]).center(35) + "|" + str(dna1_alfabeto["G"] - dna2_alfabeto["G"]).center(35) + "|" )
print ("|----------+-----------------------------------+-----------------------------------+-----------------------------------+")
print ("|        g |" + str(dna1_alfabeto["g"]).center(35) + "|"  + str(dna2_alfabeto["g"]).center(35) + "|" + str(dna1_alfabeto["g"] - dna2_alfabeto["g"]).center(35) + "|" )
print ("|----------+-----------------------------------+-----------------------------------+-----------------------------------+")


del dna1_alfabeto["A"]
del dna1_alfabeto["a"]
del dna1_alfabeto["T"]
del dna1_alfabeto["t"]
del dna1_alfabeto["C"]
del dna1_alfabeto["c"]
del dna1_alfabeto["G"]
del dna1_alfabeto["g"]


del dna2_alfabeto["A"]
del dna2_alfabeto["a"]
del dna2_alfabeto["T"]
del dna2_alfabeto["t"]
del dna2_alfabeto["C"]
del dna2_alfabeto["c"]
del dna2_alfabeto["G"]
del dna2_alfabeto["g"]

dna1_basesAmbiguas = 0
dna1_basesAmbiguas_lista = ""
for base, total in dna1_alfabeto.items():
	dna1_basesAmbiguas = dna1_basesAmbiguas + total
	dna1_basesAmbiguas_lista += base 

dna2_basesAmbiguas = 0
dna2_basesAmbiguas_lista = ""
for base, total in dna2_alfabeto.items():
	dna2_basesAmbiguas = dna2_basesAmbiguas + total
	dna2_basesAmbiguas_lista += base 

print ("|          |" + str(dna1_basesAmbiguas).center(35) + "|"  + str(dna2_basesAmbiguas).center(35) + "|" + str(dna1_basesAmbiguas - dna2_basesAmbiguas).center(35) + "|" )

print ("| Outros   +-----------------------------------+-----------------------------------+-----------------------------------+")
print ("|          |" + dna1_basesAmbiguas_lista.center(35) + "|"  + dna2_basesAmbiguas_lista.center(35) + "|" )
print ("+----------+-----------------------------------+-----------------------------------+-----------------------------------+")


