# Curso Python3 

Olá! Este material foi criado apartir das anotações feitas durante o curso de Python realizadas pelo Curso em Vídeo, do professor Gustavo Guanabara. O Python é uma linguagem moderna utilizada por grandes empresas como Google, Youtube, Globo e muitas outras.
Fácil de aprender, com código limpo e organizado, vem ganhando bastante espaço no mundo inteiro.

### Autor do Curso

- [@gustavoguanabara](https://github.com/gustavoguanabara)

### Para acompanhar os meus trabalhos: 
- [@naftaliferreira ](https://github.com/naftaliferreira)




# Arquivos

Caso queira utilizar este material para auxiliar nos estudos da linguagem, recomendo que  baixe os exercícios resolvidos para ajudar no aprendizado:
https://github.com/naftaliferreira/Curso_python_mundo1.git 

## Criação de arquivos e pastas

Para criar novos arquivos ou pastas, basta acessar a barra de navegação da idle escolhida. Você pode criar um novo arquivo clicando no botão **Novo arquivo**  . Da mesma forma pode criar uma nova pasta clicando no botão **N**.

## Trocar para outro arquivo

Todos os seus arquivos e pastas são apresentados como uma árvore no explorador de arquivos. Você pode alternar de um para outro clicando em um arquivo na árvore.

## Renomear arquivos

Você pode renomear o arquivo atual clicando no nome do arquivo na barra de navegação ou clicando no botão **Renomear** no explorador de arquivos.

## Deletar um arquivo

Você pode excluir o arquivo atual clicando no botão **Remover** no explorador de arquivos. O arquivo será movido para a pasta **Lixo** e excluído automaticamente após 7 dias de inatividade.

## Exportar um arquivo

Você pode copiar os arquivos que queira exportar de forma separada, ou copiar toda a pasta para outro dispositivo ou ambiente cloud como **Google Drive**, **Dropbox** ou outros. 

# Mundo 1 - Python

## Aula 1 - Seja um programador 
> Aula explicando as atividades e funções exercidas pelos programadores.

## Aula 2 - Para que serve o Python
> Aula explicando as diversas áreas onde o Python pode ser aplicado.

## Aula 3 - Instalando o Python3 e o IDLE
> O idle utilizado na aula é o Pycharm, a verão do Python é Python3.10.
	Porém eu optei por utilizar o VScode que é meu idle de preferência. 

## Aula 4 - Primeiros comandos no Python
> Aula onde é ensinado o famoso 'Hello World' na linguagem python.
	print('Hello World')

## Aula 5 - Instalando o Pycharm e o QPython3
> Aula apenas com informações técnicas sobre como instalar e configurar o Pycharm e o QPython3. 

### Exercício 1 - Deixando tudo pronto
> Ensinando como criar novos documentos e pastas na Idle. 

### Exercício 2 - Respondendo ao usuário
#### Função print()
A função print é utilizada para exibir o 'resultado' das ações impostas pelos programas escritos em Python. 
Dentro da linguagem esta função vem sendo mudada a cada versão para que melhor se adapte ao usuário da linguagem. 

> No Python 3.8 -:
n = 3
print('O numero é {}'.format(n))

> Já nas versões Python 3.8+:
> n = 3
> print(f'O número é {n}')

Estas são as duas formas utilizadas no Python 3, ainda são aceitas algumas funções como o print e outras da versão Python 2, porém não é recomendado utilizar, pois podem cair em desuso a qualquer momento. 

nome = input('Qual é o seu nome: ')
print(f'Prazer {nome}, seja bem vindo!')

## Aula 6 - Tipos primitivos e saída de dados

#### O que são tipos primitivos?
> int (números inteiros/ integer) = 7, -4, 0, 9875
        float (números reais / flutuantes) = 7.0, -4.0, 9875.0, 0.076
        bool (booleanos) = True, False
        str (strings) = 'caracteres entre áspas'

#### Como verificar o tipo de valor exibido?
> n1 = int(input('Digite um número: '))
        print(type(n1))
>> O comando type retorna o tipo de valor da variável.
>
>> Se não expecificar o tipo de valor ao receber os dados, automáticamente é armazenada como string, porém strings não podem ser utilizadas para operações matemáticas, pois elas concatenam.

>Outra forma de verificar os valores da variável é a função is:
>> n = input('Digite algo: ')
            print(n.isnumeric()) # Está perguntando se a variável é numerica, caso seja, retorna True, senão é False. 
            print(n.isalpha()) # Pergunta é apenas letras.
            print(n.alphanum()) # É alfanumérico?
            print(n.isupper()) # Somente letras maiusculas?
            print(n.isdecimal()) # É decimal?
            print(n.islower()) # Somente letras minusculas?
            
> Existem várias outras opções dentro do python. 

### Exercício 3 - Somando dois números

### Exercício 4 - Dissecando uma variável

## Aula 7 - Operadores Aritméticos
### Quais são os operadores?
>  Adição +
      Subtração -
      Multiplicação *
       Divisão /
        Potência ** 
        Divisão inteira // 
        Resto da divisão % 
### O que é precedência de operadores?
> 1º ( )
          2º **
          3º * / // %
          4º + -

>> A potência pode utilizando operador e também pode ser utilizado a função pow
           pow(9,2) 9**2 é 81  
>> As raizes quadrada e cúbica podem ser realizadas da seguinte forma:
            81**(1/2) = 9 # Raiz quadrada
            127**(1/3) =  5.02

>> Como utilizar operadores aritméticos com strings?
        'Oi' + 'Olá' 
         'OiOlá'
        'Oi' * 3 
         'OiOiOi'
        '=' * 10 
 >>> Desta forma as strings concatenam :
 > >>nome = Pedro
print('Prazer em te conhecer {:=^20}!'.format(nome))
Prazer em te conhecer ========== Pedro ==========
    
### Como formatar o números de casas decimais?
>  {:.2f}  No caso de formatar um número dentro da função print, com a configuração ao lado, após o ponto 2 casas flutuantes.

### Como imprimir sem quebrar a linha?
>  No print usar end = ''
>  
            n1 = 2
            n2 = 4
            s = n1 + n2
            d = n1 / n2
            print('O resultado da soma é {}'.format(s), end=' ')
            print('O resultadi da divisão é {}'.format(d))
            
>### No local de end='' vazio pode tambem colocar algo dentro dele caso queira colocar algum caractere para interagir. 

### Como quebrar a linha?
> basta usar no print \n no local onde quer quebrar a linha. 

    print('A soma é {}, \n a divião é {:.2f}'.format(s, d))

### Exercício 5 - Antecessor e Sucessor

### Exercício 6 - Dobro, Triplo, Raiz quadrada

### Exercício 7 - Média Aritmética

### Exercício 8 - Conversor de medidas

### Exercício 9 - Tabuada

### Exercício 10 - Conversor de moedas

### Exercício 11 - Pintando Parede

### Exercício 12 - Calculando descontos

### Exercício 13 - Reajuste Salarial

### Exercício 14 - Conversor de Temperaturas

### Exercício 15 - Aluguel de carros

## Aula 8 - Utilizando módulos
> Nesta aula é ensinado como utilizar módulos em Python utilizando os comandos import e from import no Python. Como carregar bibliotecas de funções e utilizar vários recursos adicionais utilizando módulos built-in e módulos externos. 
###  O que é Módulo?
#### * De maneira simples, clara e objetiva: módulo é um arquivo. Um arquivo que contém código Python. 
> Exemplo:
> math.py = trabalhar com matemática
            random.py = trabalhar com números aleatórios
            os.py = módulo para se trabalhar com arquivos
            time.py = trabalhar com tempo (dia, ano, data, etc)
            Muitos outros módulos já vem no Python por padrão.
#### Como Criar, importar e usar a função import : 
> exemplo: 
Calculadora.py

            # Esse módulo realiza as 4 operações matemáticas

            # Recebe dois números e retorna a diferença
            def soma(x,y):
                retorna x+y

            # Recebe dois números e retorna a diferença
                def subtracao(x,y):
                    return x-y

            # Recebe dois números e retorna o produto
                def multiplicacao(x,y):
                    return x*y

            # Recebe dois números e retorna a divisão do primeiro pelo segundo
                def divisao(x,y):
                    return x/y 

#### O que é função?
>>  Nada mais é que um pedaço de código, eles desenpenham funções expecíficas. Sua principal aplicação é facilitar a organização.
        Com as funções é possível desenvolver em blocos e equipes um projeto, sem necessariamente um depender do outro o tempo todo. Assim quando for necessário determinada operação é chamada uma determinada função expecífica para executar aquela operação. 
         Facilita na hora de fazer testes e também encontrar erros. 
         É possível a execução ilimitada do código
####  Como importar uma função expecífica?
> from modulo import function

 > Esta é uma forma interessante de poder trabalhar sem a necessidade de importar toda a biblioteca, se vai ser utilizado apenas 1 ou poucas funções, basta importa-las separadamente e quando for utilizar. 

#### Como gerar numeros aleatórios?
> numero inteiro aleatório, usar função randint()

import random

            continuar=1
            while continuar:
                print('Número aleatório gerado: ', random.randint(1,6))
                continuar=int(input('Gerar novamente?\n1.Sim\n0.Não\n'))
#### Como definir o melhor intervalo?
> Similar a função range, porém retorna apenas um valor, randrange()
> random.randrange(x) - vai gerar um valor aleatório entre 0 e x-1
            random.randrange(x,y) - vai gerar um número aleatório de x a y-1
            random.randrange(x,y,z) - pode gerar de x até y-1, mas ao inves de 1 em 1, vai dar salto de z em z 
#### Outros números aleatórios:
> random() - número aleatório decimal
        uniform() - retorna números floats
    Como usar o módulo math?
        math são funções matemáticas prontas, para usar basta importar. 
            import math
### Funções mais comuns: 
> cos(x) - dá o valor cosseno de x radianos
        sin(x) - valor do seno de x radianos
        tan(x) - valor da tangente de x radianos
        acos(x) - retorna o arco cosseno de x, em radianos
        asin(x) - retorna o arco seno de x, em radianos
        atan(x) - retorna o arco tangente de x, em radianos
        degrees(x) - retorna o valor em graus de x radianos
        radians(x) - retorna o contrario de degrees, pega o valor em graus e transforma em radiano. 
        sqrt(x) - raiz quadrada
        math.pi - constante pi
        floor(x) - arredonda para baixo 
        ceil(x) - arredonda para cima

### Exercício 16 – Quebrando um número

### Exercício 17 – Catetos e Hipotenusa

### Exercício 18 – Seno, Cosseno e Tangente

### Exercício 19 – Sorteando um item na lista

### Exercício 20 – Sorteando uma ordem na lista

### Exercício 21 – Tocando um MP3

## Aula 9 - Manipulando texto
### Como funciona uma string?

 frase = ['curso', 'em', 'vídeo', 'Python']
       
> No python todos os caracteres ocupam espaço, mesmo os espaços em branco são contados, cada caractere é contado com um índice de 0 até fim
> Desta forma é possível tratar dados usando a técnica de fatiamento. 

        frase[9] # retorna o nono caractere. 
        frase[9:13] # retorna da nona casa até a décima-terceira
        frase[9:21] # No fatiamento ele sempre irá exibir até o penultimo caractere, para adicionar o ultimo caracter basta colocar um dígito a mais, desde que saiba quantos dígitos tem a string.  
        frase[9:21:2] # Assim como acima, porem com a diferença que terá saltos de 2 em 2. 
        frase[:5] # Do início ao 5
        frase[15:] # do 15 ao final, caso não saiba qual será o final da string. 
        frase[9::3] # Do 9 ao fim com salto de 3 em 3.
#### Como saber o comprimento da string?
##### Com a função len
      
	 len(frase)
 
 #### Como saber a quantidade de vezes que um caractere em expecífico aparece?
    
#####  Com a função count, contando quantas vezes a letra o aparece na string.
 
	frase.count('o')


> O Python diferencia letras maiusculas e minusculas, não é a mesma coisa. 

#### Considerando do 0 a 13 quantas vezes a letra o aparece?
            frase.count('o', 0, 13)
            
#### Como encontrar um caractere específico?
##### Com a função find
	frase.find('deo')
	
>  se os caracteres forem encontrados, retorna 'True' senão, 'False'
  
#### Como verificar se um caractere ou palavra está contida na frase?
##### Função in
            'Curso' in frase 
>Se a palavra curso está na string frase, se sim, retorna 'True', senão, é 'False'
#### Como trocar caracteres dentro de uma lista?
##### com a função replace
            frase.replace('Python', 'Android')
            
> Substitui dentro da frase a palavra Python pela palavra Android. 
 
##### Com a função lower()
            frase.lower()
#### Como colocar a primeira letra em maiuscula?
#####  Com a função capitalize()
            frase.capitalize()
#### Como colocar a primeira letra de cada palavra em maiusculo?
##### Com a função title()
            frase.title()
#### Como remover espaços desnecessários?
##### Função strip(), remove todos os espaços inúteis, com exeto espaço entre palavras
            frase.strip()
#### Como remover espaços apenas do lado direito?
##### Com  a função rstrip()
            frase.rstrip()
#### Como remover espaços apenas do lado esquerdo?
##### Com a função lstrip()
            frase.lstrip()
#### Como dividir uma string?
##### com a função split()
            frase.split() 
  > onde houver espaço que separa as palavras será a divisão, e as palavras serão colocadas dentro de outra lista. 
 
#### Como juntar uma string?
##### Com a função join()
            '-'.join(frase) # Entre as palavras será colocada - .
            ' '.join(frase) # Entre as palavras será colocado espaço.
 
### Exercício 22 – Analisador de Textos

### Exercício 23 – Separando dígitos de um número

### Exercício 24 – Verificando as primeiras letras de um texto

### Exercício 25 – Procurando uma string dentro de outra

### Exercício 26 – Primeira e última ocorrência de uma string

### Exercício 27 – Primeiro e último nome de uma pessoa

## Aula 10 - Condicionais (parte 1)

> Nesta aula é ensinado como utilizar condicionais e compostas nos programas em python.
	Os programas normalmente funcionam em estrutrura sequencial, porem em condicionais nem todos os passos seram necessários.
	As condições devem estar indentadas 
	As condicionais são representadas por if e else e no final da condicional deve colocar o sinal de :
	
> Exemplo:


		tempo = int(input("Quantos anos tem seu carro? "
		if tempo <= 3:
			print('Carro Novo')
		else:
			print('Carro velho')
			
		print(' -- Fim')
		
>Existe no Python outra opção onde a condição fica em uma linha, chamado de condições simples.
	
		tempo = int(input('Quantos anos tem o seu carro? ')
		print('carro novo' if tempo <= 3 else 'carro velho')
		print('Fim')
### Exercício 28 - Jogo da adivinhação v1.0

### Exercício 29 - Radar eletrônico

### Exercício 30 - Par ou Impar

### Exercício 31 - Custo da viagem

### Exercício 32 - Ano bissexto

### Exercício 33 - Maior e menor valores 

### Exercício 35 - Analisando Triângulo v1.0

## Aula 11 - Cores no Python.
> As cores no python são adicionadas através de códigos ANSI.
	Código ANSI = escape sequence
	\033[m  para adicionar a cor, basta colocar o código da cor entre colchete e a letra m 
	
> Exemplo:

	\033[ style text back m
		
	
> style = Qual o estilo da fonte? negrito, sublinhado, italico?
	text = Qual a cor do texto?
	back = background, qual a cor de fundo?
	
> Pode colocar em qualquer ordem, pois existe diferenciação dos códigos style, text, back.
>  Os 3 são opcionais, caso não queira colocar algum detalhe. 
	Exemplo2:
	
		\033[0;33;44m
	
	style 
	0 = none
	1 = bold
	4 = underline
	7 = negative
	
	text
	30 = white
	31 = red
	32 = green
	33 = yellow
	34 = blue
	35 = purple
	36 = white blue
	37 = silver
	
	back 
	
	40 = white
	41 = red
	42 = green
	43 = yellow
	44 = blue
	45 = purple
	46 = white blue
	47 = silver


### Fim do Mundo 1 de Python