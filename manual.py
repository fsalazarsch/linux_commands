# -*- coding: utf-8 -*-
import os, json
import subprocess as sp
from collections import defaultdict

headers =[]

def agregar_header(linea):
	if linea not in headers:
		headers.append(linea)

def escribir_en_archivo(ruta, escritura):
	file1 = open( ruta,"a+")
	file1.write(escritura)
	file1.close()


def dejar_en_archivo(comando, indice):
	output = sp.getoutput('man '+comando)
	
	output = output.split("\n")

	manual = defaultdict(dict)
	index = ""

	for linea in output:
		if linea.isupper() and linea.isalpha():
			index = linea
			agregar_header(linea)
		else:
			if index != "":

				procesado = (str(manual[index]) + linea+'\n').replace("{}","")
				manual[index] =  procesado


	if not os.path.isfile("man"+str(indice)+".json"):
		escribir_en_archivo("man"+str(indice)+".json", "[")

	with open("man"+str(indice)+".json", "a+") as outfile: 
		json.dump(manual, outfile)


ruta_base =  "/usr/share/man/es";
indice = ""
#dirs=$(eval "ls -R")

commands = os.popen("ls -R "+ruta_base).read().split('\n')
commands = list(filter(lambda x: x.endswith(".gz") , commands))



for item in commands:
	item = item.split(".")

	if indice != "":
		if indice != item[-2]:
			escribir_en_archivo("man"+str(indice)+".json", "]")
		else:
			escribir_en_archivo("man"+str(indice)+".json", ",")


	indice = item[-2]
	item =  '.'.join(item).replace("."+item[-2]+".gz","")

	try:
		dejar_en_archivo(item,indice)
	except UnicodeDecodeError:
		print(item +" - "+ str(indice))


escribir_en_archivo("headers.txt", "["+", ".join(headers)+"]")