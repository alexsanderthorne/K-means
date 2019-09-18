
import csv
from pandas import DataFrame

f = open('teste+.csv', 'r')
reader = csv.reader(f)

fBin = open('binario.csv', 'r')
readerBin = csv.reader(fBin)


tabela = []
with open('teste+.csv') as csvfile:
		reader2 = csv.reader(csvfile)
		for row in reader2:
				tabela.append(row)
df = DataFrame(tabela, columns=['idade', 'cor', 'sexo', 'salario'])


maior = str(df['salario'].max())
print(len(maior))

def achaTamanho(x):
    maior = 0
    for row in readerBin:
        a = str(row[x])
        if maior < len(a):
            maior = len(a)
        
    return str(maior)

def decToBin(n,campo,i, tamanho):
	resultadoNormalizado = round((n / int(df[campo].max())) * 100)
	binario = "{0:b}".format(resultadoNormalizado)
	binarioformatado = ('{:0>{}}'.format(binario, tamanho))
	return binarioformatado

def corToBin(cor):
	global corbin
	corbin = 0
	if cor == " Branco":
			corbin = "{0:b}".format(1)
	elif cor == " Azul":
			corbin = "{0:b}".format(2)
	elif cor == " Preto":
			corbin = "{0:b}".format(3)
	elif cor == " Verde":
			corbin = "{0:b}".format(4)
	elif cor == " Roxo":
			corbin = "{0:b}".format(5)

	binarioformatado = str('{:0>4}'.format(corbin, 4))
	
	return binarioformatado

def sexoToBin(sexo):
	global sexoBin
	if sexo == " F" or sexo == " f":
			sexoBin = 1
	elif sexo == " M" or sexo == " m":
			sexoBin = 0
	return sexoBin

n = int(
    input("Digite uma opção:\n 1-Converter para binario\n 2-converter em array\n 3-"))
	
if n == 1:
	for row in reader:
		idade = int(row[0])
		cor = row[1]
		sexo = row[2]
		salario = int(row[3])
		idadeBinario = decToBin(idade, "idade", 0, 7)
		corBinario = corToBin(cor)
		sexoBinario = sexoToBin(sexo)
		salarioBinario = decToBin(salario, "salario", 3, 8)
		with open('binario.csv', 'a') as bi:
				writer = csv.writer(bi)
				writer.writerow([idadeBinario, corBinario, sexoBinario, salarioBinario])
	print("Convertido")