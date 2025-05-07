# Exercicio 1
# Letra A
cont = 1
while cont <= 10:
  print(f'{cont} x 5 = {cont * 5}')
  cont += 1


# Letra B
num = 5
for numero in range(1,11):
  print(f'{numero} x {num} = {numero * num}')

# Exercicio 2
maximo = int(input("Digite um numero inteiro positivo: "))
contador = 0
soma = 0

while contador <= maximo:

  if contador % 2 != 0:
    soma += contador

  contador += 1

print(f"A soma dos numeros impares é {soma}")

# Exercicio 3
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

for numero in range(1,11):
  print(f'{numero} x {num1} = {num1 * numero}')

print('-' * 20)

for numero in range(1,11):
  print(f'{numero} x {num2} = {num2 * numero}')
