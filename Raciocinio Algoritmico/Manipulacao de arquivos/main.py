# 1 -> Ler arquivo

with open("Manipulacao de arquivos/texto.txt", "r") as arquivo:
    # conteudo = arquivo.read()
    conteudoLinhas = arquivo.readlines()

for linha in conteudoLinhas:
    print(linha)

# print(conteudo)

# 2 -> Gravar arquivo

linha1 = "Conteudo da primeira linha\n"
linha2 = "Conteudo da segunda linha\n"

with open("Manipulacao de arquivos/texto2.txt", "w") as arquivo:
    arquivo.write(linha1)
    arquivo.write(linha2)

# 3 -> Adicionar linhas

with open("Manipulacao de arquivos/arquivo3.txt", "a") as arquivo:
    arquivo.write("texto\n")