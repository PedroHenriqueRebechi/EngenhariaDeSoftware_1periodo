# Exercicio 1
num = int(input("Digite um número: "))
if num % 2 == 0:
  print(f"O número {num} é par")
else:
  print(f"O número {num} é ímpar")

# Exercicio 2
num = int(input("Digite um número: "))
if num > 0:
  print(f"O número {num} é positivo")
elif num == 0:
  print(f"O número é 0")
else:
  print(f"O número {num} é negativo")

# Exercicio 3
letra = str(input("Digite uma letra: ")).upper()
if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
  print(f"A letra {letra} é uma vogal")
else:
  print(f"A letra {letra} é uma consoante")

# Exercicio 4
angulo1 = int(input("Digite o primeiro angulo: "))
angulo2 = int(input("Digite o segundo angulo: "))
angulo3 = int(input("Digite o terceiro angulo: "))

if angulo1 != angulo2 != angulo3:
  print("Triangulo escaleno")
elif angulo1 == angulo2 == angulo3:
  print('Triangulo equilátero')
else:
  print('Triangulo isósceles')


# Exercicio 5
salario = float(input("Digite seu salário atual: R$"))
tempoDeServico = int(input('Digite a quantidade de anos de serviço: '))

if tempoDeServico > 5:
  bonus = round(salario * (5/100),2)
  print(f"O seu salário com bônus vai ficar R${salario + bonus}")
else:
  print('Você não recebe bônus')

# Exercicio 6
valor = float(input("Digite o valor da compra: R$"))
if valor > 100.00:
  desconto = round(valor * (10/100), 2)
  print(f'O desconto é de R${desconto} e o novo valor é de R${valor - desconto}')
else:
  print("Sem desconto")

# Exercicio 7
idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
  print('Criança')
elif idade >= 13 and idade <= 17:
  print('Adolescente')
elif idade >= 18 and idade <= 59:
  print('Adulto')
elif idade >= 60:
  print('Idoso')
else:
  print('Erro')

# Exercicio 8
nota = float(input("Digite a nota do aluno: "))
if 9 <= nota <= 10:
    print("Classificação: A")
elif 7 <= nota < 9:
    print("Classificação: B")
elif 5 <= nota < 7:
    print("Classificação: C")
else:
    print("Classificação: D")