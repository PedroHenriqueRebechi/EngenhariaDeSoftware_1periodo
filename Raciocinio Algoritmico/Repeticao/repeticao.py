cont = 0
soma_medias = 0

while cont < 2:
  aluno = str(input('Digite seu nome: ')).capitalize()
  n1 = float(input('Digite um número: '))
  n2 = float(input('Digite mais um número: '))
  n3 = float(input('Digite outro número: '))
  n4 = float(input('Digite o último número: '))

  media = (n1 + n2 + n3 + n4) / 4
  soma_medias += media
  print(f'A média de {aluno} é {media}')

  if media >= 7:
    print(f'{aluno} foi Aprovado')
  else:
    print(f'{aluno} foi Reprovado')

  cont += 1
  media_total = soma_medias / cont

print(f'A média total é {media_total:.2f}')


