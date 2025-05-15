# 1
alunos = {}
alunosAprovados = {}

for aluno in range(3):
    nome = str(input('Digite o nome do aluno: '))
    nota = int(input('Digite a nota do aluno: '))
    if nota >= 7:
        alunosAprovados[nome] = nota
    alunos[nome] = nota


print(alunos)
print(alunosAprovados)

nomeAluno = str(input('Digite o nome do aluno para consultar a nota: '))

if alunos[nomeAluno] >= 7:
    print('Aprovado')
elif alunos[nomeAluno] >= 4:
    print('Recuperação')
else:
    print('Reprovado')


# 2
estoque = {}

vezes = int(input('Quantos produtos vai cadastrar: '))

for produto in range(vezes):
    nome = str(input('Digite o nome do produto: '))
    quantidade = int(input('Digite a quantidade do produto: '))
    estoque[nome] = quantidade

nomeProduto = str(input('Digite o nome do produto para consultar a quantidade: '))

for produto in estoque:
    if produto == nomeProduto:
        print('A quantidade do produto é: ', estoque[nomeProduto])
        break

nomeProdutoComprar = str(input('Digite o nome do produto que deseja comprar: '))
quantidadeProdutoComprar = int(input(f"Digite a quantidade de {nomeProdutoComprar}s que deseja comprar: "))

estoque[nomeProdutoComprar] -= quantidadeProdutoComprar

print(estoque)

# 3
frase = input("Digite uma frase: ")

frequencia = {}

for letra in frase.lower():
    if letra.isalpha():  # Ignora espaços, números e pontuação
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

print("Frequência de letras:")
print(frequencia)

# 4
votos = {}

while True:
    candidato = input("Digite o nome do candidato (ou 'fim' para encerrar): ")
    
    if candidato.lower() == 'fim':
        break

    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1


print("\nResultado da votação:")
for nome, total in votos.items():
    print(f"{nome}: {total} voto(s)")


if votos:
    vencedor = max(votos, key=votos.get)
    print(f"\nVencedor: {vencedor} com {votos[vencedor]} voto(s)")
else:
    print("\nNenhum voto registrado.")

# 5
agenda = {}

while True:
    print("\nMenu:")
    print("1 - Cadastrar contato")
    print("2 - Buscar contato")
    print("3 - Excluir contato")
    print("4 - Listar contatos")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do contato: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
        print(f"Contato '{nome}' cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome para buscar: ")
        if nome in agenda:
            print(f"{nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome para excluir: ")
        if nome in agenda:
            del agenda[nome]
            print(f"Contato '{nome}' excluído com sucesso!")
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        if agenda:
            print("\nLista de contatos:")
            for nome, telefone in agenda.items():
                print(f"{nome}: {telefone}")
        else:
            print("A agenda está vazia.")

    elif opcao == "5":
        print("Saindo da agenda...")
        break

    else:
        print("Opção inválida. Tente novamente.")

