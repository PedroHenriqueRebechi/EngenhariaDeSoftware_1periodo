# Estrutura de Repetição com Condicional 
# 1
pares = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:
        pares += 1

print(f"Quantidade de números pares: {pares}")

# 2
fim = int(input("Digite um número: "))

for i in range(1, fim + 1):
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")

# 3 
maior = None

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    if maior is None or num > maior:
        maior = num

print(f"O maior número digitado foi: {maior}")


# 4
maiores = 0

for i in range(6):
    num = float(input(f"Digite o {i+1}º número: "))
    if num > 100:
        maiores += 1

print(f"Quantidade de números maiores que 100: {maiores}")


# 5
soma_pares = 0
quantidade_pares = 0

while True:
    num = int(input("Digite um número positivo (ou um negativo para parar): "))
    if num < 0:
        break
    if num % 2 == 0:
        soma_pares += num
        quantidade_pares += 1

if quantidade_pares > 0:
    media = soma_pares / quantidade_pares
    print(f"Média dos números pares: {media}")
else:
    print("Nenhum número par foi digitado.")


# LISTAS    
# 1
nomes = []

while True:
    nome = str(input("Digite um nome: "))
    nomes.append(nome)
    nomes.sort()
    status = str(input("Deseja continuar? (sim/nao): "))
    if status == 'sim':
        continue
    elif status == 'nao':
        break

print(nomes)
    
# 2
notas = []

for i in range(6):
    nota = float(input("digite sua nota: "))
    notas.append(nota)
    i += 1

somaNotas = sum(notas)
media = somaNotas / len(notas)

print(notas)
print(media)


# 3
lista = []
n = int(input('Quantos numeros quer adicionar a lista: '))

for numero in range(n):
    num = int(input('Digite o numero: '))
    lista.append(num)

maiorNumero = None

for numero in lista:
    if maiorNumero is None or numero > maiorNumero:
        maiorNumero = numero

print(maiorNumero)


# 4
numeros = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = sum(numeros)
print(f"A soma dos números é: {soma}")

# 5
lista = []

for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    lista.append(num)

maiores_que_cinco = [n for n in lista if n > 5]

print("Números maiores que 5:", maiores_que_cinco)



# DICIONÁRIOS
# 1

dic = {
    'pedro': 18,
    'joao': 22,
    'laura': 21
}


for i in dic:
    print(dic[i])

print(dic.values())

# 2
pessoas = {}

for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    pessoas[nome] = idade

print("\nDicionário de pessoas:", pessoas)

# 3 
frutas = {
    'maçã': 3.50,
    'banana': 2.00,
    'laranja': 4.00
}

frutas.update({'banana': 2.50})

print("Dicionário atualizado de frutas:", frutas)


# 4
dados = {'chave1': 'valor1', 'chave2': 'valor2'}

dados.clear()
print("Depois do clear:", dados)

# 5
carro = {
    'marca': 'Toyota',
    'modelo': 'Corolla',
    'ano': 2022
}

print("Chaves:", carro.keys())
print("Valores:", carro.values())
print("Itens:", carro.items())


# Multipla escolha
# 1 B
# 2 D
# 3 C
# 4 B
# 5 B
# 6 C
# 7 C