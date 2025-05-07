# Primeiro Programa
print("Olá mundo!")

# Segundo programa
idade = int(input("Digite a sua idade: "))
print(f"Sua idade é {idade}")

# Terceiro programa
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
sub = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2
print(f"O resultado é = Soma: {soma} = Sub: {sub} = Mult: {mult} = Div: {div}")

# Quarto programa
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")