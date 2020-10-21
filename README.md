# pari2021_TP1_Grupo10

// Instruções especiais para o asciidoc usar icons no output
:icons: html5
:iconsdir: /etc/asciidoc/images/icons

Nota 1: É necessário ter um repositório git só para este trabalho. Todos os elementos do grupo devem trabalhar sobre o mesmo repo (serem colaboradores).

Nota 2: No dia da apresentação (quarta-feira, durante a aula) cada grupo apresentará por ordem aleatória. As apresentações serão à base de demonstração e não do código em si. No entanto, o prof pode pedir para ver o código e o repositório github

Nota 3: o professor pode (e vai) fazer perguntas a todos os membros do grupo, ou possívelmente aos 2 que não falarem na apresnetação. Para avaliar se todos percebem o que foi feito

Nota 4: todos os elementos do mesmo grupo terão a mesma nota

Nota 5: a aprentação será de cerca de 10 minutos, entre perguntas e explicaç

Intruções do Trabalho:

Aula 4 - PARI
=============
Miguel Riem Oliveira <mriem@ua.pt>
2020-2021

// Instruções especiais para o asciidoc usar icons no output
:icons: html5
:iconsdir: /etc/asciidoc/images/icons


.Sumário
-------------------------------------------------------------
Avaliação - escrita de um programa para testes de typing.
-------------------------------------------------------------

PARI Typing Test
----------------

Deve desenvolver um programa similar a um https://www.typingtest.com/[typing test].

Em resumo, o programa deve mostrar ao utilizador letras geradas de forma aleatória, ficando depois à espera que o utilizador insira a letra indicada. Quando o utilizador insere uma letra, o programa passa para a letra seguinte até que o desafio atinja uma tempo máximo predefinido.

Veja este vídeo exemplificativo do https://youtu.be/6tRTOd5vPH8[programa em execução]

Dealhadamente, as funcionalidades a desenvolver são as seguintes:

1. criar um ficheiro main.py com a estrutura habitual

2. o programa deve receber dois argumentos de entrada que definem o modo de finalização do teste (tempo máximo ou número de inputs máximo).

[TIP]
========================================================
[source,Bash]
--------------------------------------------------------
usage: main.py [-h] [-utm] [-mv MAX_VALUE]

Definition of test mode

optional arguments:
  -h, --help            show this help message and exit

  -utm, --use_time_mode
                        Max number of secs for time mode or maximum number of inputs for number of inputs mode.

  -mv MAX_VALUE, --max_value MAX_VALUE
                        Max number of seconds for time mode or maximum number of inputs for number of inputs mode.
--------------------------------------------------------
========================================================

[start=3]
. o programa deve pedir ao utilizador que pressione uma tecla para começar o desafio
. Depois de iniciado o desafio, o programa mostra uma letra minúscula (gerada aleatoreamente) ao utilizador e aguarda o input do utilizador (um caracter apenas, sem o utilizador ter de pressionar o enter)
. o funcionamento do teste deverá ter dois modos distintos: tempo máximo ou número de inputs máximo. O teste deve continuar até que seja ativada uma das seguintes condições de paragem:
    .. No modo de tempo máximo, quando o tempo de teste decorrido for maior do que o tempo máximo definido
    .. No modo de número de inputs máximo, quando o número de inputs dado pelo utilizador atingir o máximo predefinido
    .. Quando o utilizador pressiona a tecla "espaço", o que leva à interrupção do teste (em qualquer dos modos)
. Depois de cada input do utilizador, o programa deve imprimir uma mensagem indicando a tecla pressionada pelo utilizador e se foi ou não a correta
. Para cada evento de input deve ser guardada a seguinte informação: letra mostrada (requested); letra recebida (received); tempo decorrido desde que é mostrada a letra até ao input do utilizador (duration).

[TIP]
===================================
 Defina um _namedtuple_ chamado _Input_ que contenha os três campos acima enumerados.
===================================

[start=8, bold]
. Depois de terminada a inserção de entradas, calcular várias estatisticas do teste, descritas na tabela seguinte:

[width="80%"]
|===================================================
|Parâmetro | Descrição

| test_duration | duração total do teste
| test_start | Data de início do teste
| test_end | Data de término do teste
| number_of_types | número de inputs
| number_of_hits | número de inputs corretos
| accuracy | precisão de inputs (hits/total)
| type_average_duration | duração média das respostas do utilizador
| type_hit_average_duration | duração média das respostas corretas do utilizador
| type_miss_average_duration | duração média das respostas incorretas do utilizador
|===================================================

Deve criar um dicionário python com todos estes campos, mais um campo adicional que é uma lista namedtuples do _Input_ (ver acima). Um exemplo do dicionario criado:

[source,Bash]
--------------------------------------------------------
{'accuracy': 0.0,
 'inputs': [Input(requested='v', received='s', duration=0.11265206336975098),
            Input(requested='w', received='d', duration=0.07883906364440918),
            Input(requested='d', received='a', duration=0.0720210075378418),
            Input(requested='a', received='s', duration=0.0968179702758789),
            Input(requested='b', received='d', duration=0.039067983627319336)],
 'number_of_hits': 0,
 'number_of_types': 5,
 'test_duration': 0.3997969627380371,
 'test_end': 'Thu Sep 10 16:36:20 2020',
 'test_start': 'Thu Sep 10 16:36:20 2020',
 'type_average_duration': 0.07987945793212418,
 'type_hit_average_duration': 0.0,
 'type_miss_average_duration': 0.07987945793212418}

--------------------------------------------------------

[start=9]
. o programa deve, antes de finalizar, imprimir o dicionário que foi criado

[TIP]
=======================================================================
Depois de criar o dicionario pode imprimi-lo com um simple

[source,Python]
--------------------------------------------------------
print(my_dict)
--------------------------------------------------------

No entanto, para ficar com uma impressão mais perceptível pode usar o package https://docs.python.org/3/library/pprint.html[prettyprint]:

[source,Python]
--------------------------------------------------------
from pprint import pprint
pprint(my_dict)
--------------------------------------------------------

=======================================================================

Avaliação
---------
A avaliação será feita com base na existência e qualidade das funcionalidades acima descritas. A organização e legibilidade do código também poderá ser tida em conta.
---------