import math
import cmath

# Questão 1
print("Equação 1: √(2x² + 5x - 3) / (y - 2)")
while True:
    try:
        x_str = input("Digite o valor de x: ")
        x = float(x_str)
        y_str = input("Digite o valor de y: ")
        y = float(y_str)
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite números para x e y.")

expressao_raiz = 2 * x**2 + 5 * x - 3

if expressao_raiz >= 0 and y != 2:
    resultado = math.sqrt(expressao_raiz) / (y - 2)
    print("O resultado é:", resultado)
elif expressao_raiz < 0 and y != 2:
    resultado = cmath.sqrt(expressao_raiz) / (y - 2)
    print("O resultado (complexo) é:", resultado)
elif y == 2 and expressao_raiz < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo e dividir por zero.")
else:
    print("Não é possível dividir por zero.")

# Questão 2
print("\nEquação 2: |x - 2y| * log10(z + 1) / √(x² + y² - 5)")
while True:
    try:
        x_str = input("Digite o valor de x: ")
        x = float(x_str)
        y_str = input("Digite o valor de y: ")
        y = float(y_str)
        z_str = input("Digite o valor de z: ")
        z = float(z_str)
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite números para x, y e z.")

denominador = x**2 + y**2 - 5
argumento_log = z + 1

if denominador > 0 and argumento_log > 0:
    resultado = abs(x - 2 * y) * math.log10(argumento_log) / math.sqrt(denominador)
    print("O resultado é:", resultado)
elif denominador == 0:
    print("Não é possível dividir por zero (denominador igual a zero).")
elif denominador < 0 and argumento_log <= 0:
    print("Não é possível calcular: a raiz quadrada do denominador seria negativa e o argumento do logaritmo não seria positivo.")
elif denominador < 0:
    print("Não é possível calcular porque a raiz quadrada do denominador seria de um número negativo.")
else:  # argumento_log <= 0
    print("Não é possível calcular porque o argumento do logaritmo não seria positivo.")

# Questão 3
print("\nEquação 3: resultado = sin(ângulo) / (cos(ângulo) - 1)")
while True:
    try:
        angulo_graus_str = input("Digite o valor do ângulo em graus: ")
        angulo_graus = float(angulo_graus_str)
        angulo_radianos = math.radians(angulo_graus)
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o ângulo.")

if not math.isclose(math.cos(angulo_radianos), 1.0, rel_tol=1e-9):
    resultado = math.sin(angulo_radianos) / (math.cos(angulo_radianos) - 1)
    print("O resultado é:", resultado)
else:
    print("Não é possível dividir por zero, pois o cosseno do ângulo resulta em 1.")
