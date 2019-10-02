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
	'contatoLinguagem', 'linguagem', 'razao'])

with open('binario.csv') as csvfile:
    reader2 = csv.reader(csvfile)
    for row in reader2:
        tabela.append(row)
df2 = DataFrame(tabela, columns=['sexo', 'idade', 'cidadeNatal', 'cidadeReside', 'estadoCivil', 'cor',
	'meioTransporte', 'transportePublico', 'salario', 'ingles', 'atividadeRemunerada', 'escola', 'curso',
	'contatoLinguagem', 'linguagem', 'razao'])

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

def decToBin2(n,campo,i, tamanho):
	resultadoNormalizado = int(n) #round((n / int(df2[campo].max())) * 100)
	binario = "{0:b}".format(resultadoNormalizado)
	binarioformatado = ('{:0>{}}'.format(binario, tamanho))
	return binarioformatado

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
	elif sexo == "Outro":
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
linguagemBin = 0
def liguagemToBin2(linguagem):
		if linguagem == "Java, Java Script, PORTUGOL":
				linguagemBin = "{0:b}".format(9)
		elif linguagem == "Java, Python, C, Ruby":
				linguagemBin = "{0:b}".format(10)
		elif linguagem == "Java, C, C++, C#":
				linguagemBin = "{0:b}".format(11)
		elif linguagem == "Java, PHP, Java Script, Angular":
				linguagemBin = "{0:b}".format(12)
		elif linguagem == "C, C++, C#, Java Script":
				linguagemBin = "{0:b}".format(13)
		elif linguagem == "Java, Python, C++, PHP, JSF":
				linguagemBin = "{0:b}".format(14)
		elif linguagem == "Java, Python, C, Java Script, Angular, Dart":
				linguagemBin = "{0:b}".format(15)
		elif linguagem == "Java, C, C++, Java Script, Angular":
				linguagemBin = "{0:b}".format(16)
		elif linguagem == "Java, Python, C, C++, C#, PHP, .NET, Java Script, Dart (Flutter)":
				linguagemBin = "{0:b}".format(17)
		return linguagemBin
		

def liguagemToBin(linguagem):
	if linguagem == "":
			linguagemBin = "{0:b}".format(0)
	elif linguagem == "Java":
			linguagemBin = "{0:b}".format(1)
	elif linguagem == "Python":
			linguagemBin = "{0:b}".format(2)
	elif linguagem == "C++":
			linguagemBin = "{0:b}".format(3)
	elif linguagem == "Visual Basic":
			linguagemBin = "{0:b}".format(4)
	elif linguagem == "Python, Java Script":
			linguagemBin = "{0:b}".format(5)
	elif linguagem == "Java, Java Script":
			linguagemBin = "{0:b}".format(6)
	elif linguagem == "Java, Python, C":
			linguagemBin = "{0:b}".format(7)
	elif linguagem == "Python, C, Java Script":
			linguagemBin = "{0:b}".format(8)
	else:
		linguagemBin = liguagemToBin2(linguagem)
		
	binarioformatado = str('{:0>5}'.format(linguagemBin))
	return binarioformatado

def razaoToBin2(razao):
	if razao == "Mercado aquecido na área de tecnologia (razões financeiras), Afinidade com a área de tecnologia, Possibilidade de abrir minha própria empresa (por exemplo, uma startup)":
			razaoBin = "{0:b}".format(9)
	elif razao == "Mercado aquecido na área de tecnologia (razões financeiras), Afinidade com a área de tecnologia, Possibilidade de trabalhar em grandes centros (no Brasil ou no exterior), Possibilidade de abrir minha própria empresa (por exemplo, uma startup)":
			razaoBin = "{0:b}".format(10)
	elif razao == "Influência de amigos/familiares, Mercado aquecido na área de tecnologia (razões financeiras), Possibilidade de trabalhar em grandes centros (no Brasil ou no exterior), Possibilidade de abrir minha própria empresa (por exemplo, uma startup)":
			razaoBin = "{0:b}".format(11)
	elif razao == "Influência de amigos/familiares, Mercado aquecido na área de tecnologia (razões financeiras), Afinidade com a área de tecnologia, Possibilidade de trabalhar em grandes centros (no Brasil ou no exterior), Possibilidade de abrir minha própria empresa (por exemplo, uma startup)":
			razaoBin = "{0:b}".format(12)
	elif razao == "Mercado aquecido na área de tecnologia (razões financeiras), Afinidade com a área de tecnologia, Possibilidade de trabalhar em grandes centros (no Brasil ou no exterior), Possibilidade de abrir minha própria empresa (por exemplo, uma startup)":
			razaoBin = "{0:b}".format(13)
	elif razao == "Afinidade com a área de tecnologia, Possibilidade de abrir minha própria empresa (por exemplo, uma startup), Crescer profissionalmente e usar os novos conhecimentos adquiridos no meu local de trabalho.":
			razaoBin = "{0:b}".format(14)
	elif razao == "Mercado aquecido na área de tecnologia (razões financeiras)":
			razaoBin = "{0:b}".format(15)
	return razaoBin

def razaoToBin(razao):
	if razao == "Possibilidade de abrir minha própria empresa (por exemplo, uma startup)":
			razaoBin = "{0:b}".format(1)
	elif razao == "Afinidade com a área de tecnologia":
			razaoBin = "{0:b}".format(2)
	elif razao == "Mercado aquecido na área de tecnologia (razões financeiras)":
			razaoBin = "{0:b}".format(3)
	elif razao == "mudanca ou ascensão profissional na empresa em q trabalho":
			razaoBin = "{0:b}".format(4)
	elif razao == "Influência de amigos/familiares, Afinidade com a área de tecnologia":
			razaoBin = "{0:b}".format(5)
	elif razao == "Afinidade com a área de tecnologia, Possibilidade de abrir minha própria empresa (por exemplo, uma startup)":
			razaoBin = "{0:b}".format(6)
	elif razao == "Mercado aquecido na área de tecnologia (razões financeiras), Afinidade com a área de tecnologia":
			razaoBin = "{0:b}".format(7)
	elif razao == "Afinidade com a área de tecnologia, Possibilidade de trabalhar em grandes centros (no Brasil ou no exterior), Possibilidade de abrir minha própria empresa (por exemplo, uma startup)":
			razaoBin = "{0:b}".format(8)
	else:
		razaoBin = razaoToBin2(razao)
	
	binarioformatado = str('{:0>5}'.format(razaoBin))
	return binarioformatado
	
def normaliza(num, campo):
    num = int(df.iloc[reader.line_num][campo])
    resultado = round((num / int(df[campo].max())) * 100)
    return resultado

n = int(input("Digite uma opção:\n 1-Converter para binario\n 2-Converter idade"))
	
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
		contatoLinguagem = row[13]
		linguagem = row[14]
		razao = row[15]

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
		contatoLinguagemBinario = trueOrFalse(contatoLinguagem)
		linguagemBinario = liguagemToBin(linguagem)
		razaoBinario = razaoToBin(razao)


		with open('binario.csv', 'a') as bi:
			writer = csv.writer(bi)
			writer.writerow([sexoBinario, idadeDecimal, cidadeNatalBinario, cidadeResideBinario,
			estadoCivilBinario, corBinario, meioTransporteBinario, transportePublicoBinario,
			salarioBinario, inglesBinario, atividadeRemuneradaBinario, escolaBinario,
			cursoBinario, contatoLinguagemBinario, linguagemBinario, razaoBinario])
if n ==2:
		for row in readerBin:
			sexo = row[0]
			idade = row[1]
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
			contatoLinguagem = row[13]
			linguagem = row[14]
			razao = row[15]
			
		
			idadeDecimal2 = decToBin2(idade, "idade", 1, 7)
			with open('bin.csv', 'a') as bi2:
				writer2 = csv.writer(bi2)
				writer2.writerow([sexo, idadeDecimal2, cidadeNatal, cidadeReside,
				estadoCivil, cor, meioTransporte, transportePublico,
				salario, ingles, atividadeRemunerada, escola,
				curso, contatoLinguagem, linguagem, razao])