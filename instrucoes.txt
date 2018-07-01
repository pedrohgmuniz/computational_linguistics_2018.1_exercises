Instruções para o trabalho de final de semestre.
Deverá ser feito em equipe com um total de três alunos matriculados e a participação de ouvintes.
O funcionamento dos programas deverá ser demonstrado em sala de aula. (Não teremos mais tempo para isso.)
Deverá ser enviada por e-mail a documentação dos programas elaborados juntamente com o código fonte dos programas.

-----------------------------------------------------

TAREFA 1:

Seja o seguinte exemplo: 

"O menininho comia, bem devagarinho, com uma colherzinha, a comidinha preparada com carinho por sua mãezinha, para depois poder tomar o sorvetinho bem geladinho e comer o pudim de aipim."
Em dialetos populares do Brasil, por exemplo, em determinados falares nordestinos, ocorrem pronúncias como "meninim" para "menininho" ou "sorvetim" para "sorvetinho". 

1) Faça uma pesquisa sobre esse fenômeno, procurando determinar se se trata de um fenômeno lexical ou fonológico desses dialetos. Dica: consulte um atlas linguístico de um estado brasileiro, como, por exemplo, o atlas linguístico do Ceará ou de outro estado do Nordeste.

2) Em seguida, adotando o esquema para elaboração de programas proposto pelo livro a respeito da linguagem piton: Elabore uma função em linguagem piton que faça conversão da forma culta para a forma popular.
Elabore diferentes versões dessa função:
a) A primeira versão será limitada a palavras isoladas. 
b) A segunda versão deverá ser capaz de tomar uma sentença como entrada. 
c) A terceira versão deverá ser capaz de lidar com sinais de pontuação.
d) Elabore outra função capaz de realizar a conversão inversa, ou seja, da linguagem popular para a linguagem culta. Implemente uma estratégia pouco custosa e eficiente para lidar com as exceções a essa conversão.
Dica: consulte o léxico de formas plenas:  https://github.com/LFG-PTBR/MorphoBr
Coloque todas as funções em um módulo, capaz de ser executado também a partir da linha de comando do terminal do sistema operacional Unix!
Reflita: qual seria a utilidade prática de um programa que realizasse esses dois tipos de conversão?


-----------------------------------------------------


TAREFA 2:

OBS: ESTA TAREFA JÁ ESTÁ FEITA. Já temos diversas versões dos programas. Elas podem, no entanto, serem aperfeiçoadas.

Construir em Prologue ou linguagem piton:
a) Parte 1: detector de palíndromo:

palindrome("Ana")
True

palindrome("arara")
True

palindrome("amora")
False

palindrome("O galo ama o lago")
True


b) Parte 2: detector de anagramas

anagram("amora","aroma")
True

anagram("ator","rota")
True 

anagram("Iracema","América")
True

anagram("ator","rato")
True 

anagram("ator","rata")
False


-----------------------------------------------------


TAREFA 3:

PARTE 1) Extrair 500 diminutivos aleatórios do seguinte recurso lexical:

https://github.com/LFG-PTBR/MorphoBr/tree/master/diminutives

Construir uma função em linguagem piton capaz de realizar a extração de um dado número aleatório de linhas de uma lista de arquivos especificados, salvando o resultado em um arquivo.

ExtractRandomLines(1500,infile1,infile2)

Observação: essa parte da tarefa poderá ser compartilhada pelas três equipes. 
Dica: usar a ferramenta split do sistema operacional Unix pra dividir o arquivo de 1500 linhas em três arquivos de 500 linhas.

Em seguida, cada equipe deverá fazer uma revisão dos 500 diminutivos da lista que lhe coube, Incluindo uma terceira coluna com as letras g para gramatical e a para agramatical. Os casos considerados não gramaticais deverão ser explicados num documento à parte. Essa tarefa deverá ser realizada por 3 membros da equipe, cujos nomes deverão ser especificados na documentação.


PARTE 2) A partir da leitura de trabalhos recentes na área de morfologia do português, identifique lacunas sistemáticas no recurso lexical 
https://github.com/LFG-PTBR/MorphoBr ,
decorrentes de regras produtivas de formação de palavras. Por exemplo, esse recurso contém as seguintes palavras: uvada, abacatada, mangada, cajuada, bananada e umbuzada mas não jabuticabada, graviolada ou maracujazada (https://repositorio.unesp.br/bitstream/handle/11449/94045/santos_gg_me_assis.pdf;sequence=1)
Apresente exemplos da internet ou de outras fontes abonando algumas das lacunas identificadas.
As equipes devem combinar entre si para não trabalhar com os mesmos processos produtivos.
Depois de identificar os processos de criação de novas palavras, construir um programa em Prologue ou em linguagem piton capaz de gerar os pares de forma flexionada e fazer análise lexical, tal como nós temos no recurso lexical mencionando.
As contribuições das três equipes deverão ser disponibilizadas sob licença livre em repositório próprio no Github, descrevendo no arquivo README, de forma breve, o recurso e especificando os nomes de todos que contribuíram.