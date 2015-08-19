import argparse

print ("<INICIO>") 

#recuperar os parametros do argumento
parser = argparse.ArgumentParser()
parser.add_argument("arquivo1", type=argparse.FileType('r'))
parser.add_argument("arquivo2", type=argparse.FileType('r'))
args = parser.parse_args()
arquivo1 = args.arquivo1
arquivo2 = args.arquivo2

dna1_conteudo = ""
dna2_conteudo = ""

dna1_cabecalho = ""
dna2_cabecalho = ""

os_dnas_sao_iguais = True

for tmp_linhaAtual in arquivo1:
	if (tmp_linhaAtual[0] == '>' or tmp_linhaAtual[0] == '@'):
		dna1_cabecalho = dna1_cabecalho + '\n' + tmp_linhaAtual.strip()
	else:
		dna1_conteudo = dna1_conteudo + tmp_linhaAtual.strip()
dna1_conteudo = list(dna1_conteudo)

for tmp_linhaAtual in arquivo2:
	if (tmp_linhaAtual[0] == '>' or tmp_linhaAtual[0] == '@'):
		dna2_cabecalho = dna2_cabecalho + '\n' + tmp_linhaAtual.strip()
	else:
		dna2_conteudo = dna2_conteudo + tmp_linhaAtual.strip()

for x in range(0, len(dna1_conteudo)):
	if( dna1_conteudo[x] != dna2_conteudo[x] ):
		os_dnas_sao_iguais = False

print("Arquivo 1....................: " +      arquivo1.name   )
print("Cabecalho(s)...............: " +      dna1_cabecalho   )

print("Arquivo 2....................: " +      arquivo2.name   )
print("Cabecalho(s)...............: " +      dna2_cabecalho   )

print("São iguais?...........: " + str(os_dnas_sao_iguais))

print ("<TERMINO>")














