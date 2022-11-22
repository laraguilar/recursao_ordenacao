'''
Trabalho Prático
Recursão e Ordenação
Disciplina: Programação II
Professor: Hilário Seibel
Grupo: Gabriely Moro e Lara Aguilar
'''

import pickle
import os
import comparar as c

# função responsável por ordenar os alunos por nota e avaliar critérios de desempate
def ordenaAlunos(alunos):
  matr = []  # lista com a matricula dos alunos
  notas = []  #lista com as notas

  # cria a lista de matriculas e de notas
  for aluno in alunos:
    matr.append(aluno)
    n1, n2, n3 = alunos[aluno][2][0], alunos[aluno][2][1], alunos[aluno][2][2]
    faltas = alunos[aluno][3]
    total = n1 + n2 + n3
    total += verificaBonus(total, faltas) #soma a nota com o bonus
    notas.append(total) 


  # chama o método de ordenação
  quickSort(notas, 0, len(notas) - 1, matr, alunos)

  # verifica os empates de acordo com os critérios
  desempate(notas, matr, alunos)
  return matr

# Método de ordenação QuickSort
def quickSort(notas, inf, sup, matr, dic):
  if inf < sup:
    pos = particao(notas, inf, sup, matr, dic)
    quickSort(notas, inf, pos - 1, matr, dic)
    quickSort(notas, pos + 1, sup, matr, dic)

# particao do metodo QuickSort, responsável por encontrar a
# posição original do número
def particao(l, inf, sup, matr, dic):
  pivot = l[inf]
  i, j = inf + 1, sup
  while i <= j:
    while i <= j and l[i] > pivot:
      i += 1
    while j >= 1 and l[j] < pivot:
      j -= 1
    if i <= j:
      troca(l, i, j, matr)
      i += 1
  troca(l, inf, j, matr)
  return j

# Efetua a troca de posições em uma lista
def troca(l, x, y, matr):
  # troca de posicao das notas
  aux = l[x]
  l[x] = l[y]
  l[y] = aux
  #troca de posicao da matricula
  aux = matr[x]
  matr[x] = matr[y]
  matr[y] = aux
  return 0

# desempate por matrícula, ultimo criterio
def desempateMatricula(matr1, matr2):
  # cria uma lista e ordena de acordo com a matricula
  l = [matr1, matr2]
  l = sorted(l)

  #verifica qual vem primeiro
  if l[0] == matr1:
    return matr1
  return matr2

# desempate em ordem alfabética do nome
def desempAlfabetico(matr1, matr2, dic):
  l = []
  nome1 = dic[matr1][0]
  nome2 = dic[matr2][0]

  #Se os nomes forem iguais, segue para o próximo critério
  if nome1 == nome2:
    return desempateMatricula(matr1, matr2)

  # cria uma lista com os dois nomes
  l = [nome1, nome2]

  # ordena em ordem alfabética
  l = sorted(l)

  # verifica quem vem primeiro
  if l[0] == matr1:
    return matr1
  return matr2

# desempate pelo semestre antigo
def desempateSemestre(matr1, matr2, dic):
  a1, p1 = dic[matr1][1]
  a2, p2 = dic[matr2][1]

  # classifica do mais recente ao mais antigo 
  if a1 > a2: return matr1
  if a2 > a1: return matr2
  if p1 > p2: return matr1
  if p2 > p1: return matr2
    
  # caso ainda haja empate, segue para o próximo critério
  return desempAlfabetico(matr1, matr2, dic)

# Desempate por nota sem o bônus
def desempateNota(matr1, matr2, dic):
  n1A, n2A, n3A = dic[matr1][2]
  n1B, n2B, n3B = dic[matr2][2]
  n1 = n1A + n2A + n3A
  n2 = n1B + n2B + n3B

  #verifica se as notas, sem bonus, são maior ou menor
  if n1 > n2: return matr1
  if n2 > n1: return matr2

  # caso as notas ainda sejam iguais, segue para o próximo critério
  return desempateSemestre(matr1, matr2, dic)


def desempate(notas, matr, alunos):
  for i in range(len(notas) - 1):
    if notas[i] == notas[i + 1]:
      primeiro = desempateNota(matr[i], matr[i + 1], alunos)
      if (primeiro != matr[i]):
        # realiza a troca, se necessário, de acordo com o desempate
        troca(notas, i, i + 1, matr) 
  return 0

# verifica qual o bônus do aluno
def verificaBonus(total, faltas):
  if (faltas == 0 and total <= 98):
    return 2
  elif (total == 99):
    return 1
  return 0

def busca(x, l):
  inicio = 0
  fim = len(l) - 1

  while inicio <= fim:
    meio= (inicio + fim) // 2
    if l[meio] == x:
        return meio
    elif l[meio] > x:
        inicio = meio + 1
    elif l[meio] < x:
        fim = meio - 1      
  return -1

def verificaAprovados(matr, alunos):
  notas = []
  for matricula in matr:
    n1, n2, n3 = alunos[matricula][2]
    faltas = alunos[matricula][3]
    total = n1 + n2 + n3
    total += verificaBonus(total, faltas) #soma a nota com o bonus
    notas.append(total) 

  apr = busca(60, notas)
  alunosApr = notas[:apr+1]
  aprovados = len(alunosApr)   
  print(aprovados)


def saida(lMatricula, alunos):
  with open('saida.txt', 'w') as f:
    for matr in lMatricula:
      nome, _, notas, faltas = alunos[matr]
      n1, n2, n3 = notas
      total = n1 + n2 + n3
      if verificaBonus(total, faltas) != 0:
        f.write(f'{nome} - {total} +{verificaBonus(total, faltas)}\n')
      else:
        f.write(f'{nome} - {total}\n')
  return 0


# leitura do arquivo binário e retorna dicionário com os dados
def readArq():
  arquivo = 'entrada100000.bin'
  if os.path.isfile(arquivo):
    with open(arquivo, 'rb') as arq:
      dic = pickle.load(arq)
    return dic

# programa principal
def main():
  alunos = readArq()
  matr = ordenaAlunos(alunos)
  saida(matr, alunos)
  verificaAprovados(matr, alunos)
  c.compararSaidas('saida.txt', 'saida100000.txt')
  #print(alunos)
  return 0


if __name__ == '__main__':
  main()

#('Miguel de Caminha', (2011, 2), (24, 12, 22), 30),

#'BSI1021526': ('Francisca Guimarães', (2014, 2), (14, 21, 5), 12),