## Tecnologias utilizadas:

    Linguagem de programação: Python
    Bibliotecas:
    * Pandas
    * Seaborn
    * Matplotlib
    * KMeans
    * NumPy
    * SciPy

Análise de dados não supervisionados da turma de ADS IFPE 2019.2

Objetivo: Identificar similaridades entre os alunos da turma de Análise e Desenvolvimento de Sistemas do IFPE - Campus Garanhuns, utilizando técnicas de Machine Learning e Data Mining.

Dados:

    Foram utilizados dados de 29 estudantes da 1º turma de ADS.
    As variáveis analisadas incluem sexo, idade, cidade natal, cidade de residência, estado civil, cor, meio de transporte, transporte público, salário, inglês, atividade remunerada, escola, curso, contato em outra linguagem, linguagem de interesse e razão para cursar ADS.

Metodologia:

    Importação e pré-processamento dos dados:
        Os dados foram importados de um arquivo CSV utilizando a biblioteca Pandas.
        As variáveis categóricas foram codificadas numericamente.
        A idade foi normalizada.

    Análise exploratória de dados:
        Análise descritiva das variáveis.
        Visualização dos dados através de gráficos e tabelas.

    Algoritmo K-Means:
        O algoritmo K-Means foi utilizado para agrupar os alunos em clusters com base em suas características.
        O número ideal de clusters foi determinado utilizando o método do "cotovelo".

    Análise dos clusters:
        As características dos alunos de cada cluster foram analisadas.
        As diferenças entre os clusters foram identificadas.

Resultados:

    A análise identificou 2 grupos distintos de alunos.
    O Grupo 1 é composto por alunos mais jovens, solteiros, que residem na cidade natal e utilizam transporte público. Eles geralmente possuem um nível de renda mais baixo e menor proficiência em inglês.
    O Grupo 2 é composto por alunos mais velhos, casados, que residem em outra cidade e utilizam transporte próprio. Eles geralmente possuem um nível de renda mais alto e maior proficiência em inglês.

Conclusão:

A análise de dados não supervisionados permitiu identificar similaridades entre os alunos da turma de ADS IFPE 2019.2. Os resultados podem ser utilizados para direcionar ações pedagógicas e de apoio aos alunos, visando melhorar o processo de ensino-aprendizagem.

Observações:

    Este README é um resumo da análise realizada. Para mais detalhes, consulte o código Python e os relatórios de análise.
    As análises e conclusões apresentadas neste README são baseadas nos dados específicos utilizados na pesquisa.

Melhorias realizadas:

    Estrutura mais clara e organizada:
        Adição de subtítulos para facilitar a leitura.
        Uso de marcadores para destacar pontos importantes.
    Texto mais informativo:
        Explicação mais detalhada das etapas da análise.
        Adição de informações sobre os resultados obtidos.
        Inclusão de conclusões e observações relevantes.
    Visualização aprimorada:
        Remoção de código Python desnecessário.
        Adição de descrições para as tabelas e gráficos.
    Linguagem mais acessível:
        Evitar termos técnicos excessivos.
        Usar linguagem clara e concisa.

Próximos passos:

    Realizar análises mais aprofundadas dos clusters identificados.
    Explorar outras técnicas de Machine Learning e Data Mining para a análise dos dados.
    Coletar dados de outras turmas para comparar os resultados.

Agradecimentos:

    Agradeço aos alunos da turma de ADS IFPE 2019.2 por terem disponibilizado seus dados para esta pesquisa.
    Agradeço à equipe do IFPE - Campus Garanhuns pelo apoio.
