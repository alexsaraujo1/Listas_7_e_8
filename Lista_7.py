# Exercicios

# 1. Construa um programa no qual o usuário informe o nome, a estatura e o peso de vários alunos
# de uma turma. Após o cadastro, o programa deve imprimir o nome e o IMC de cada aluno ordenados
# pelo nome do aluno. Sabe-se que IMC = peso/altura**2

Feito em sala

# Turma = {'nome':[],
#         'estatura':[],
#         'peso':[],
#         'IMC':[]}

# nome = input('Insira um nome:')
# estatura = float(input('Insira estatura:'))
# peso = float(input('Insira o peso: '))
# IMC = peso/estatura**2
# i = '1'
# while i != '0':
#     Turma['nome'].append(nome)
#     Turma['estatura'].append(estatura)
#     Turma['peso'].append(peso)
#     Turma['IMC'].append(IMC)
#     i = input('Se deseja continuar digite qualquer tecla, se deseja parar digite 0: ')
#     if i == '0':
#         break
#     nome = input('Insira um nome:')
#     estatura = float(input('Insira estatura:'))
#     peso = float(input('Insira o peso: '))
#     IMC = peso/estatura**2

# print(Turma)

# 2. Faça um script que receba os valores do nome, idade e e-mail de uma pessoae guarde-os em um dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. Exiba as informações desse dicionário

nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))
email = input('Qual é o seu e-mail? ')

pessoa = {'nome': nome, 'idade': idade, 'email': email}

print('As informações da pessoa são as seguintes:')
print(pessoa)


# 3. Faça um programa que leia 10 números do usuário e os coloque corretamente no dicionário D abaixo.
# D = {'pares': [], 'impares':[]}


# Crie um dicionário vazio
numeros = {}
# Crie o dicionário
D = {"pares": [], "impares": []}

# Leia 10 números do usuário
for i in range(10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        D["pares"].append(numero)
    else:
        D["impares"].append(numero)

# Imprima o dicionário
print(D)


# 4. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos
# de mercado e seus respectivos preços e os mostre na tela.



total = {"produtos": [], "preços": []}
for i in range(1):
    produtos = input("Informe o nome do produto:")
    preços = int(input("Digite o valor do produto: "))

total_produtos={'produtos':produtos, 'preços':preços}

print("Os produtos e seus repectivos preços são em reais:")

print(total_produtos)

# 5. Escreva um programa que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde achave é a vogal considerada.

vogais = 'aeiou'
s = 'agora'
qtd_vogais = 0
for c in s.lower():
    if c in vogais:
        qtd_vogais += 1
print(qtd_vogais) 

# 6. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo
#  como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).

semana = {}
semana = {'segunda':'python',
        'terça':'metodologia',
        'quarta':'python',
        'quinta':'python',
        'sexta':'',
        'sabado':'',
        'domingo':'',
}
print(semana)