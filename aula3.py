# FUNÇÕES BUILT-IN EM PYTHON #

# print() é uma função built-in do interpretador Python.
## Uma função built-in é um objeto que está integrado ao núcleo do interpretador, ou seja, não precisa ser feita nenhuma instalação adicional, já está pronto para uso.
### Ao observar o quadro abaixo, podemos identificar algumas funções que já usamos:
#print(), para imprimir um valor na tela.
#enumerate(), para retornar a posição de um valor em uma sequência.
#input(), para capturar um valor digitado no teclado.
#int() e float(), para converter um valor no tipo inteiro ou float.
#range(), para criar uma sequência numérica.
#type(), para saber qual o tipo de um objeto (variável).

print("Hello World")

# A função eval() usada no código recebe como entrada uma string (sequência de caracteres) digitada pelo usuário, que nesse caso é uma equação linear. Essa entrada é analisada e avaliada como uma expressão Python pela função eval(). Veja que, para cada valor de x, a fórmula é executada como uma expressão matemática e retorna um valor diferente.
## A função eval() foi mostrada a fim de exemplificar a variedade de funcionalidades que as funções built-in possuem. Entretanto, precisamos ressaltar que eval é uma instrução que requer prudência para o uso, pois é fácil alguém externo à aplicação fazer uma "injection" de código intruso.
a=2
b=1

equacao=input("Digite a fórmula geral da equação lineara (a*x+b):")
print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")
for x in range(5):
    y=eval(equacao)
    print(f"\nResultado da equação para x={x} é {y}")

# O interpretador Python possui várias funções disponíveis, veja o quadro a seguir.
## abs(); all(); any(); ascii(); bin(); bool(): breakpoint(); bytearray(); bytes(); callable(); 
## chr(); cassmethod(); compile(); complex(); delattr();dict(); dir(); divmod(); enumerate(); eval()
## exec(); filter(); float(); format(); frozenset(); getattr(); globals(); hasattr(); hash(); help()
## hex(); id(); input(); int(); isinstance(); issubclass(); iter(); len(); list(); locals(); map()
## max(); memoryview(); min(); next(); object(); oct(); open(); ord(); pow(); print(); property(); 
## range(); repr(); reversed(); round(); set(); setattr(); slice(); sorted(); staticmethod(); str();
## sum(); super(); tuple(); type(); vars(); zip(); _import__()




# FUNÇÃO DEFINIDA PELO USUÁRIO #

# Python possui 70 funções built-in (quadro abaixo), que facilitam o trabalho do desenvolvedor, porém cada solução é única e exige implementações específicas. Diante desse cenário, surge a necessidade de implementar nossas próprias funções, ou seja, trechos de códigos que fazem uma determinada ação e que nós, como desenvolvedores, podemos escolher o nome da função, sua entrada e sua saída.
## Para que uma função execute suas ações, ela precisa ser "invocada", fazemos isso na linha 39, colocando o nome da função, acompanhada dos parênteses.
def imprimir_mensgem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na disciplica: {disciplina}, do curso: {curso}.")

imprimir_mensgem("Linguagem de Programação","Engenharia de Software")


# O que acontece se tentarmos atribuir o resultado da função "imprimir_mensagem" em uma variável, por exemplo:
# resultado = imprimir_mensagem("Python", "ADS")? Como a função "imprimir_mensagem" não possui retorno, a variável "resultado" receberá "None".
def imprimir_mensgem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na disciplica: {disciplina}, do curso: {curso}.")

resultado=imprimir_mensgem("Linguagem de Programação","Engenharia de Software")
print(f"Resultado={resultado}")


# Para que o resultado de uma função possa ser guardado em uma variável, a função precisa ter o comando "return". A instrução "return", retorna um valor de uma função. Veja a nova versão da função "imprimir_mensagem", agora, em vez de imprimir a mensagem, ela retorna a mensagem para chamada.
# Veja na linha 55 da entrada que, em vez de imprimir a mensagem, a função retorna (return) um valor para quem a invocou. O uso do "return" depende da solução e das ações que se deseja para a função.
## Por exemplo, podemos criar uma função que limpa os campos de um formulário, esse trecho pode simplesmente limpar os campos e não retornar nada, mas também pode retornar um valor booleano como True, para informar que a limpeza aconteceu com sucesso. Portanto, o retorno deve ser analisado, levando em consideração o que se espera da função e como se pretende tratar o retorno, quando necessário.
def imprimir_mensgem(disciplina, curso):
    return f"Minha primeira função em Python desenvolvida na disciplica: {disciplina}, do curso: {curso}."

mensagem = imprimir_mensgem("Linguagem de Programação","Engenharia de Software")
print(mensagem)

# Vamos implementar uma função que recebe uma data no formato dd/mm/aaaa e converte o mês para extenso. Então, ao se receber a data 15/08/2023, a função deverá retornar: 15 de agosto de 2023. Observe a implementação a seguir.
def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) -1] # O mês 1, estará na posição 0!
    return f'{d} de {mes_extenso} de {a}'
print(converter_mes_para_extenso('15/08/2023'))
##Linha 61 - Definimos o nome da função e os parâmetros que ela recebe.
##Linha 62 - Criamos uma lista com os meses, por extenso. Veja que criamos uma string e usamos a função split(), que "quebra" a string a cada espaço em branco, criando uma lista e elementos.
##Linha 63 - Usamos novamente a função split(), mas agora passando como parâmetro o caractere '/', isso quer dizer que a string será cortada sempre que ele aparecer. Nessa linha também usamos a atribuição múltipla. Ao cortar a string 'dd/mm/aaaa', temos uma lista com três elementos: ['dd', 'mm', 'aaaa'], ao usar a atribuição múltipla, cada valor da lista é guardado dentro de uma variável, na ordem em que foram declaradas. Então d = 'dd', m = 'mm', a = 'aaaa'. O número de variáveis tem que ser adequado ao tamanho da lista, senão ocorrerá um erro.
##Linha 64 - Aqui estamos fazendo a conversão do mês para extenso. Veja que buscamos na lista "mes" a posição m - 1, pois, a posição inicia em 0. Por exemplo, para o mês 8, o valor "agosto", estará na setima posição da lista "mes".
##Linha 65 - Retornamos a mensagem, agora com o mês em extenso.
##Linha 66 - Invocamos a função, passando como parâmetro a data a ser convertida.




# FUNÇÕES COM PARÂMETROS DEFINIDOS E INDEFINIDOS #

# Sobre os argumentos que uma função pode receber, para nosso estudo, vamos classificar em seis grupos:
# 1- parâmetro posicional, obrigatório, sem valor default (padrão).
# 2- parâmetro posicional, obrigatório, com valor default (padrão).
# 3- parâmetro nominal, obrigatório, sem valor default (padrão).
# 4- parâmetro nominal, obrigatório, com valor default (padrão).
# 5- parâmetro posicional e não obrigatório (args).
# 6- parâmetro nominal e não obrigatório (kwargs).

# No grupo 1, temos os parâmetros que vão depender da ordem em que forem passados, por isso são chamados de posicionais (a posição influencia o resultado). Os parâmetros desse grupo são obrigatórios, ou seja, tentar invocar a função, sem passar os parâmetros, acarreta um erro. Além disso, os parâmetros não possuem valor default.
def somar(a,b):
    return a+b
r = somar(2,3)
print(r)
## A função "somar" na linha 93 foi definida de modo a receber dois parâmetros, porém na linha 95, quando ela foi invocada, somente um parâmetro foi passado, o que resultou no erro "missing 1 required positional argument", que traduzindo quer dizer: "falta 1 argumento posicional obrigatório". Para que a função execute sem problema, ela deve ser invocada passando os dois argumentos, por exemplo: r = somar(2, 3)

# No grupo 2, também temos os parâmetros posicionais e obrigatórios, porém vamos definir um valor default (padrão), assim, quando a função for invocada, caso nenhum valor seja passado, o valor default é utilizado.
def calcular_desconto(valor, desconto=0): #O parâmetro desconto possui zero valor default
    valor_com_desconto=valor-(valor*desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) #Não aplicar nenhum desconto
valor2 = calcular_desconto(100, 0.25) #Aplicar desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")
# A função "calcular_desconto" na linha 100 foi definida de modo a receber dois parâmetros: "valor" e "desconto". O parâmetro "valor" não possui valor default, já o parâmetro "desconto" possui zero como valor default, ou seja, se a função for invocada e o segundo parâmetro não for passado, será usado o valor padrão definido para o argumento. Veja que, na linha 104, a função é invocada, sem passar o segundo argumento e não causa erro, pois existe o valor default. Já na linha 105 a função é invocada passando tanto o valor quanto o desconto a ser aplicado.




# OS ERROS #

# A obrigatoriedade do argumento, quando não atendida, pode resultar em um erro, conforme visto anteriormente. Porém, para o conceito de parâmetros posicionais não existe nenhum erro de interpretação associado, ou seja, o interpretador não irá informar o erro, mas pode haver um erro de lógica.
def cadastrar_pessoa(nome, idade, cidade):
    print("\nDados a serem cadastrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

cadastrar_pessoa("João", 23, "São Paulo")#Retorno da função como esperamos
cadastrar_pessoa("São Paulo", "João", 23)#Retorno da função como esperamo, porém com erro de lógica

# O grupo 3 é caracterizado por ter parâmetros nominais, ou seja, agora não mais importa a posição dos parâmetros, pois eles serão identificados pelo nome, os parâmetros são obrigatórios, ou seja, na chamada da função é obrigatório passar todos os valores e sem valor default (padrão).
def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()
    
texto = converter_maiuscula(flag_maiuscula=True, texto="João") # Passagem nominal de parâmetros
print(texto) 
#A função "converter_maiuscula" na linha 127 foi definida de modo a receber dois parâmetros: "texto" e "flag_maiuscula". Caso "flag_maiuscula" seja True, a função deve converter o texto recebido em letras maiúsculas, com a função built-in upper(), caso contrário, em minúsculas, com a função built-in lower(). Como a função "converter_maiuscula" não possui valores default para os parâmetros, então a função deve ser invocada passando ambos valores.

# O grupo 4 é similar ao grupo 3: parâmetro nominal, obrigatório, mas nesse grupo os parâmetros podem possuir valor default (padrão).
def converter_minuscula(texto, flag_minuscula=True): # O parâmetro flag_minuscula possui True como valor default
    if flag_minuscula:
        return texto.lower()
    else:
        return texto.upper()

texto1 = converter_minuscula(flag_minuscula=True, texto="LINGUAGEM de Programação")
texto2 = converter_minuscula(texto="LINGUAGEM de Programação")

print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")
#A função "converter_minuscula" na linha 140 foi definida de modo a receber dois parâmetros, porém um deles possui valor default. O parâmetro flag_minuscula, caso não seja passado na chamada da função, receberá o valor True. 
#Veja a chamada da linha 145, passamos ambos os parâmetros, mas na chamada da linha 146, passamos somente o texto. Para ambas as chamadas o resultado foi o mesmo, devido o valor default atribuído na função. Se não quiséssemos o comportamento default, aí sim precisaríamos passar o parâmetro, por exemplo: texto = converter_minuscula(flag_minuscula=False,texto="LINGUAGEM de Programação").

# No grupo 5, temos parâmetros posicionais indefinidos, ou seja, a passagem de valores é feita de modo posicial, porém a quantidade não é conhecida.
def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for i, valor in enumerate(args):
        print(f"posição = {i}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros("São Paulo", 10, 23.78, "João")

print("\nChamada 2")
imprimir_parametros(10, "São Paulo")
#A função "imprimir_parametros" na linha 154 foi definida de modo a obter parâmetros arbitrários. Tal construção é feita, passando como parâmetro o *args. O parâmetro não precisa ser chamado de args, mas é uma boa prática. Já o asterisco antes do parâmetro é obrigatório. 
#Na linha 155, usamos a função built-in len() (length) para saber a quantidade de parâmetros que foram passados. Como se trata de parâmetros posicionais não definidos, conseguimos acessar a posição e o valor do argumento, usando a estrutura de repetição for e a função enumerate(). Agora observe as chamadas feitas nas linhas 162 e 165, cada uma com uma quantidade diferente de argumentos, mas veja na saída que os argumentos seguem a ordem posicional, ou seja, o primeiro vai para a posição 0, o segundo para a 1 e assim por diante.

# O grupo 6 possui parâmetro nominal e não obrigatório. O mecanismo é parecido com as do grupo 5, porém agora a passagem é feita de modo nominal e não posicional, o que nos permite acessar tanto o valor do parâmetro quanto o nome da variável que o armazena.
def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor = {valor}")      

print("\nChamada 1")
imprimir_parametros(cidade="São Paulo", idade=33, nome="João")

print("\nChamada 2")
imprimir_parametros(desconto=10, valor=100)
#A função "imprimir_parametros" na 170 foi definida de modo a obter parâmetros nominais arbitrários. Tal construção é feita, passando como parâmetro o **kwargs. O parâmetro não precisa ser chamado de kwargs, mas é uma boa prática. Já os dois asteriscos antes do parâmetro é obrigatório. 
#Na linha 171, estamos imprimindo o tipo de objeto recebido, você pode ver na saída que é um dict (dicionário), o qual estudaremos nas próximas aulas. Na linha 172, usamos a função built-in len() (length) para saber a quantidade de parâmetros que foram passados. Como se trata de parâmetros nominais não definidos, conseguimos acessar o nome da variável em que estão atribuídos o valor e o próprio valor do argumento, usando a estrutura de repetição "for" e a função items() na linha 175. 
#A função items não é built-in, ela pertence aos objetos do tipo dicionário, por isso a chamada é feita como "kwargs.items()" (ou seja, objeto.função). Agora observe as chamadas feitas nas linhas 179 e 182, cada uma com uma quantidade diferente de argumentos, mas veja na saída que os argumentos estão associados ao nome da variável que foi passado.




# FUNÇÕES ANÔNIMAS EM PYTHON #
#Já que estamos falando sobre funções, não podemos deixar de mencionar um poderoso recurso da linguagem Python: a expressão "lambda". Expressões lambda (às vezes chamadas de formas lambda) são usadas para criar funções anônimas. Uma função anônima é uma função que não é construída com o "def" e, por isso, não possui nome. Esse tipo de construção é útil, quando a função faz somente uma ação e é usada uma única vez.

(lambda x:x+1)(x=3)
#Na 192, criamos uma função que recebe como parâmetro um valor e retorna esse valor somado a 1. Para criar essa função anônima, usamos a palavra reservada "lambda" passando como parâmetro "x". O dois pontos é o que separa a definição da função anônima da sua ação, veja que após os dois pontos, é feito o cálculo matemático x + 1. Na frente da função, já a invocamos passando como parâmetro o valor x=3, veja que o resultado é portanto 4.

(lambda x,y: x+y)(x=3, y=2)
#Na linha 195, criamos uma função anônima que recebe como parâmetro dois valores e retorna a soma deles. Para criar essa função anônima, usamos a palavra reservada "lambda" passando como parâmetro "x, y". Após os dois pontos, é feito o cálculo matemático x + y. Na frente da função, já a invocamos passando como parâmetro o valor x=3 e y=2, veja que o resultado é portanto 5.

# A linguagem Python, nos permite atribuir a uma variável uma função anônima, dessa forma, para invocar a função, fazemos a chamada da variável. 
somar = lambda x,y: x+y
somar(x=5, y=3)
#Na linha 200, criamos uma função anônima que recebe como parâmetro dois valores e retorna a soma deles, essa função foi atribuída a uma variável chamada "somar". Veja que na linha 201, fazemos a chamada da função através do nome da variável, passando os parâmetros que ela requer.

#Breve exercício
#Em seu novo projeto, você foi designado a implementar uma solução que envolve o cálculo de uma compra. Para esse cálculo existem parâmetros que são obrigatórios e outros opcionais, portanto a função deve ser capaz de lidar com esse tipo de dinâmica.
def calcular_valor(valor_prod, qtde, moeda="real", desconto=None, acrescimo=None):

    v_bruto = valor_prod * qtde

    

    if desconto:

        v_liquido = v_bruto - (v_bruto * (desconto / 100))

    elif acrescimo:

        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))

    else:

        v_liquido = v_bruto

    

    if moeda == 'real':

        return v_liquido

    elif moeda == 'dolar':

        return v_liquido * 5

    elif moeda == 'euro':

        return v_liquido * 5.7

    else:

        print("Moeda não cadastrada!")

        return 0


    

valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)

print(f"O valor final da conta é {valor_a_pagar}")

#Sobre a solução proposta, observe o nome da função "calcular_valor", veja que estamos seguindo as recomendações de nomenclatura, usando somente letras em minúsculo e com o underline separando as palavras. Outro detalhe é a utilização do verbo no infinitivo "calcular", toda função executa ações, por isso, é uma boa prática escolher verbos infinitos.
#A função foi desenvolvida de modo a receber cinco parâmetros, sendo três deles obrigatórios e dois opcionais. Nessa implementação, para construir os parâmetros opcionais atribuímos o valor None às variáveis, nesse caso, como tem um valor padrão, mesmo sendo None, a função pode ser invocada sem a passagem desses parâmetros.
#Usamos as estruturas condicionais (if) para verificar se foram passados valores para desconto ou acréscimo, caso tenha valores, serão diferentes de None e, então, os devidos cálculos são realizados. Após os cálculos de desconto, é feito o teste para saber qual moeda foi usada na compra e fazer a conversão para real.
#Muitas vezes, uma solução pode ser implementada de diferentes formas. Observe no código a seguir uma outra implementação, usando o **kwargs para os argumentos opcionais. Nesse caso, um dicionário é recebido e precisa ter o valor extraído. Na próxima aula, você aprenderá esse tipo de objeto.
def calcular_valor(valor_prod, qtde, moeda="real", **kwargs):

    v_bruto = valor_prod * qtde

    

    if 'desconto' in kwargs:

        desconto = kwargs['desconto']

        v_liquido = v_bruto - (v_bruto * (desconto / 100))

    elif 'acrescimo' in kwargs:

        acrescimo = kwargs['acrescimo']

        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))

    else:

        v_liquido = v_bruto

    

    if moeda == 'real':

        return v_liquido

    elif moeda == 'dolar':

        return v_liquido * 5

    elif moeda == 'euro':

        return v_liquido * 5.7

    else:

        print("Moeda não cadastrada!")

        return 0


    

valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)

print(f"O valor final da conta é {valor_a_pagar}")