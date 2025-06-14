dados = []

dados.append("Maçã")
dados.append("Banana")
dados.append("Laranja")

dados[1] = "Uva"

dados.remove("Laranja")

with open("dados.txt", "w") as arquivo:
    for item in dados:
        arquivo.write(item + "\n")