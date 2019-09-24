import csv
from pandas import DataFrame
from datetime import date
import dateutil.parser as parser

f = open('dados.csv', 'r')
reader = csv.reader(f)

fBin = open('binario.csv', 'r')
readerBin = csv.reader(fBin)
count = 1
tabela = []
with open('dados.csv') as csvfile:
    reader2 = csv.reader(csvfile)
    for row in reader2:
        tabela.append(row)
df = DataFrame(tabela, columns=['sexo', 'idade', 'cidadeNatal', 'cidadeReside', 'estadoCivil', 'cor',
	'meioTransporte', 'transportePublico', 'salario', 'ingles', 'atividadeRemunerada', 'escola', 'curso',
	'linguagem'])

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
		(birthDate.month, birthDate.day))
    return age

def achaTamanho(x):
    maior = 0
    for row in readerBin:
        a = str(row[x])
        if maior < len(a):
            maior = len(a)
        print(a)
    return str(maior)



def decToBin(n,campo,i, tamanho):
	resultadoNormalizado = round((n / int(df[campo].max())) * 100)
	binario = "{0:b}".format(resultadoNormalizado)
	binarioformatado = ('{:0>{}}'.format(binario, tamanho))
	return binarioformatado
	
def trueOrFalse(campo):
	if campo == "Não":
			valorBin = 0
	elif campo == "Sim":
			valorBin = 1
	return valorBin


def corToBin(cor):
	if cor == "Branco":
			corbin = "{0:b}".format(1)
	elif cor == "Pardo":
			corbin = "{0:b}".format(2)
	elif cor == "Negro":
			corbin = "{0:b}".format(3)
	elif cor == "Amarelo":
			corbin = "{0:b}".format(4)

	binarioformatado = str('{:0>3}'.format(corbin))
	return binarioformatado


def sexoToBin(sexo):
	if sexo == "Masculino":
			sexobin = "{0:b}".format(1)
	elif sexo == "Feminino":
			sexobin = "{0:b}".format(2)
	elif sexo == "Outros":
			sexobin = "{0:b}".format(3)
	elif sexo == "Não desejo informar":
			sexobin = "{0:b}".format(4)

	binarioformatado = str('{:0>3}'.format(sexobin))
	return binarioformatado

def cidadeToBin(cidade):
	if cidade == "Garanhuns":
			cidadeBin = "{0:b}".format(1)
	if cidade == "Recife":
			cidadeBin = "{0:b}".format(2)
	if cidade == "São Paulo":
			cidadeBin = "{0:b}".format(3)
	if cidade == "Alagoa Grande":
			cidadeBin = "{0:b}".format(4)
	if cidade == "Iati":
			cidadeBin = "{0:b}".format(5)
	if cidade == "Natal":
			cidadeBin = "{0:b}".format(6)
	if cidade == "Brejão":
			cidadeBin = "{0:b}".format(7)
	if cidade == "São João":
			cidadeBin = "{0:b}".format(8)
	if cidade == "Caruaru":
			cidadeBin = "{0:b}".format(9)
	if cidade == "Lajedo":
			cidadeBin = "{0:b}".format(10)
	if cidade == "Jucati":
			cidadeBin = "{0:b}".format(11)

	binarioformatado = str('{:0>4}'.format(cidadeBin))
	return binarioformatado

def estadoCivilToBin(estadoCivil):
	if estadoCivil == "Solteiro":
			estadoCivilbin = "{0:b}".format(1)
	elif estadoCivil == "Casado":
			estadoCivilbin = "{0:b}".format(2)
	elif estadoCivil == "União Estável":
			estadoCivilbin = "{0:b}".format(3)

	binarioformatado = str('{:0>3}'.format(estadoCivilbin))
	return binarioformatado

def salTobin(salario):
	if salario == "Até R$ 1.254":
			salariobin = "{0:b}".format(1)
	elif salario == "R$ 1.255  até R$ 2.004":
			salariobin = "{0:b}".format(2)
	elif salario == "R$ 2.005 até R$ 8.640":
			salariobin = "{0:b}".format(3)

	binarioformatado = str('{:0>3}'.format(salariobin))
	return binarioformatado

def inglesToBin(nivel):
	if nivel == "Nada":
			nivelbin = "{0:b}".format(1)
	elif nivel == "Pouco":
			nivelbin = "{0:b}".format(2)
	elif nivel == "Intermediário":
			nivelbin = "{0:b}".format(3)
	elif nivel == "Avançado":
			nivelbin = "{0:b}".format(4)

	binarioformatado = str('{:0>3}'.format(nivelbin))
	return binarioformatado

def escolaToBin(escola):
	if escola == "Escola Pública":
			escolabin = "{0:b}".format(1)
	elif escola == "Escola Privada":
			escolabin = "{0:b}".format(2)
	elif escola == "Instituto Federal (IF)":
			escolabin = "{0:b}".format(3)
	elif escola == "Escola pública integral":
			escolabin = "{0:b}".format(4)

	binarioformatado = str('{:0>3}'.format(escolabin))
	return binarioformatado

def cursoToBin(curso):
	if curso == "Não":
			cursoBin = "{0:b}".format(1)
	if curso == "Sim, fiz um curso técnico/IF.":
			cursoBin = "{0:b}".format(2)
	if curso == "Sim, já cursei um curso na área de tecnologia.":
			cursoBin = "{0:b}".format(3)
	if curso == "Comecei outro curso de tecnologia mas desisti":
			cursoBin = "{0:b}".format(4)
	if curso == "Iniciei curso técnico/IF, mas não terminei.":
			cursoBin = "{0:b}".format(5)
	if curso == "Fiz BCC na UFRPE, mas desisti.":
			cursoBin = "{0:b}".format(6)
	if curso == "Curso superior incompleto":
			cursoBin = "{0:b}".format(7)
	if curso == "Fiz mas não concluí":
			cursoBin = "{0:b}".format(8)

	binarioformatado = str('{:0>4}'.format(cursoBin))
	return binarioformatado

def normaliza(num, campo):
    num = int(df.iloc[reader.line_num][campo])
    resultado = round((num / int(df[campo].max())) * 100)
    return resultado

n = int(input("Digite uma opção:\n 1-Converter para binario\n 2-teste"))
	
if n == 1:
	for row in reader:
		sexo = row[0]
		idade = row[1]
		ano = parser.parse(idade).year
		mes = parser.parse(idade).month
		dia = parser.parse(idade).day
		anoIdade = calculateAge(date(ano, mes, dia))
		cidadeNatal = row[2]
		cidadeReside = row[3]
		estadoCivil = row[4]
		cor = row[5]
		meioTransporte = row[6]
		transportePublico = row[7]
		salario = row[8]
		ingles = row[9]
		atividadeRemunerada = row[10]
		escola = row[11]
		curso = row[12]
		linguagem = row[13]

		sexoBinario = sexoToBin(sexo)
		idadeDecimal = anoIdade #decToBin(anoIdade, "idade", 1, 7)
		cidadeNatalBinario = cidadeToBin(cidadeNatal)
		cidadeResideBinario = cidadeToBin(cidadeReside)
		estadoCivilBinario = estadoCivilToBin(estadoCivil)
		corBinario = corToBin(cor)
		meioTransporteBinario = trueOrFalse(meioTransporte)
		transportePublicoBinario = trueOrFalse(transportePublico)
		salarioBinario = salTobin(salario)
		inglesBinario = inglesToBin(ingles)
		atividadeRemuneradaBinario = trueOrFalse(atividadeRemunerada)
		escolaBinario = escolaToBin(escola)
		cursoBinario = cursoToBin(curso)
		linguagemBinario = trueOrFalse(linguagem)

		with open('binario.csv', 'a') as bi:
			writer = csv.writer(bi)
			writer.writerow([sexoBinario, idadeDecimal, cidadeNatalBinario, cidadeResideBinario,
			estadoCivilBinario, corBinario, meioTransporteBinario, transportePublicoBinario,
			salarioBinario, inglesBinario, atividadeRemuneradaBinario, escolaBinario,
			cursoBinario, linguagemBinario])
	print("convertido")
if n ==2:
	print("teste")
		# for row in reader:
		# 	idade = row[1]
		# 	ano = parser.parse(idade).year
		# 	mes = parser.parse(idade).month
		# 	dia = parser.parse(idade).day
		# 	anoIdade = calculateAge(date(ano, mes, dia))
		# 	idadeDecimal2 = 3 #decToBin(anoIdade, "idade", 1, 7)
		# 	with open('bin.csv', 'a') as bi2:
		# 		writer2 = csv.writer(bi2)
		# 		writer2.writerow([sexoBinario, idadeDecimal2, cidadeNatalBinario, cidadeResideBinario,
		# 		estadoCivilBinario, corBinario, meioTransporteBinario, transportePublicoBinario,
		# 		salarioBinario, inglesBinario, atividadeRemuneradaBinario, escolaBinario,
		# 		cursoBinario, linguagemBinario])