#!/usr/bin/python
import MySQLdb
import os.path
import time
import argparse
from verifEntrada import verificarEntrada
from listConstructor import newlist
from VerifTamDoBloco import verificarbloco

parser = argparse.ArgumentParser()
parser.add_argument("fastafile")
args = parser.parse_args()
arquivo = args.fastafile
arquivoEntrada = open(arquivo, 'r')

minSize = int(input("Type the minimum block size:\n"))
maxSize = int(input("Type the maximum block size:\n"))

stringNative = ""
for conteudo_linhaAtual in arquivoEntrada:
	if (conteudo_linhaAtual[0] == '>' or conteudo_linhaAtual[0] == '@' or conteudo_linhaAtual[0] == '#'):
		conteudo_linhaAtual.strip()	
	else:
		stringNative = stringNative + conteudo_linhaAtual.strip()

stringNative = list(stringNative.upper())
Run = verificarEntrada (minSize, maxSize)
working = True

if (Run == True):
	#Opening the database
	db = MySQLdb.connect("localhost","root","root","Genes")
	cursor = db.cursor()
	#Genome table
	sql = "INSERT INTO genoma(arquivo) VALUES ('%s')"%(arquivo)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
		working = False

	if (working == True):
		for sizeBlock in range (minSize, maxSize+1):
			#Batery Table
			cursor.execute("SELECT max(id_genoma) FROM genoma")
			resultadoDoSelect = cursor.fetchone()
			id_genoma = resultadoDoSelect[0]
			print("id_genoma: " + str(id_genoma))

			sql = "INSERT INTO bateria (id_genoma, tamanho_bloco) VALUES (%d,%d)"%(id_genoma, sizeBlock)
			cursor.execute(sql)

			try:
				cursor.execute(sql)
				db.commit()
			except:
				db.rollback()
				working = False

			if (working == True):
				for startPosition in range (0, sizeBlock):
					#Execucao Table
					sql = "SELECT * FROM bateria WHERE = id_bateria(select max(id_bateria) from bateria)"
					idg = cursor.fetchall()
					id_bateria = idg[0]
					sql = "INSERT INTO execucao(id_bateria, deslocamento) VALUES ('%d, %d')"%(id_bateria, startPosition)
					try:
						cursor.execute(sql)
						db.commit()
					except:
						db.rollback()
						working = False

					if (working == True):
						posCriar = verificarbloco(sizeBlock,len(stringNative),startPosition)
						if (posCriar == True):
							stringFinal = newlist(sizeBlock, startPosition, stringNative)
							for v in range (0, len(stringFinal)):
								if (working == True):
									sql = "SELECT * FROM execucao WHERE = id_execucao(select max(id_execucao) from execucao)"
									idg = cursor.fetchall()
									id_execucao = idg[0]
									if (v == 0):
										if (startPosition == 0):
											sql = "INSERT INTO bloco(id_execucao, arquivo, bloco_posicao, bloco_tamanho) \
											VALUES ('%d, %s, %d, %d')"%(id_execucao, stringFinal[v], startPosition, sizeBlock)
										else:
											sql = "INSERT INTO bloco(id_execucao, arquivo, bloco_posicao, bloco_tamanho) \
											VALUES ('%d, %s, %d, %d')"%(id_execucao, stringFinal[v], startPosition, startPosition)
									else:
										if(v == (len(stringFinal - 1))):
											sql = "INSERT INTO bloco(id_execucao, arquivo, bloco_posicao, bloco_tamanho) \
											VALUES ('%d, %s, %d, %d')"%(id_execucao, stringFinal[v], startPosition, len(stringFinal[v]))
										else:
											sql = "INSERT INTO bloco(id_execucao, arquivo, bloco_posicao, bloco_tamanho) \
											VALUES ('%d, %s, %d, %d')"%(id_execucao, stringFinal[v], startPosition, sizeBlock)
								try:
									cursor.execute(sql)
									db.commit()
								except:
									db.rollback()
									working = False
else:
	print ("This values are not possible")
if (working == False):
	print("AN ERROR HAS OCCORED WHILE ACESSING THE DATABASE")
db.close()