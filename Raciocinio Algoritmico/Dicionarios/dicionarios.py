dic = {"Joao":"a", "Maria": "b"}
s = "%(Joao)s e %(Maria)s"
print(s%dic)

# Limpando dicionário
dic.clear()
print(dic)


dic2 = {}.fromkeys([2,3])
print(dic2)

dic2 = dict.fromkeys(["Joao","Maria"], 0)
print(dic2)


dic3 = {}

quantidade = int(input('Quantos pares de chave:valor você quer adicionar? '))

for i in range(quantidade):
    chave = input('Digite a chave: ')
    valor = input('Digite o valor: ')
    dic3[chave] = valor

print(dic3)