'''
Trabalho Prático
Recursão e Ordenação
Disciplina: Programação II
Professor: Hilário Seibel
Grupo: Gabriely Moro e Lara Aguilar
'''

import pickle
import os
#import comparar as c

#função responsável por ordenar a matrícula dos alunos de acordo com suas notas 
def ordenaAlunos(alunos):
  matr = []
  # gera a lista de matricula
  for aluno in alunos:
    matr.append(aluno)
  # funcao de ordenacao 
  mergesort(matr, alunos)
  return matr

def mergesort(l, alunos):
  if len(l)>1:
    tam = len(l)//2
    lEsq = l[:tam]
    lDir = l[tam:]
    mergesort(lEsq, alunos)
    mergesort(lDir, alunos)
    merge(l, lEsq, lDir, alunos)

# funcao responsavel por comparar e juntar as listas
def merge(l, lEsq, lDir, alunos):
  i = 0
  j = 0
  k = 0
  while len(lEsq)>i and len(lDir)>j:
    # verifica qual nota é maior para efetuar a troca de posição
    if compara(lEsq[i], lDir[j], alunos):
      l[k] = lEsq[i]
      i+= 1
    else:
      l[k] = lDir[j]
      j += 1
    k += 1 
  while len(lEsq) > i:
    l[k] = lEsq[i]
    k += 1
    i += 1
  while len(lDir) > j:
    l[k] = lDir[j]
    k += 1
    j += 1

# compara duas notas e realiza o desempate, se necessário
def compara(matr1, matr2, alunos):
  n1A, n2A, n3A = alunos[matr1][2]
  n1B, n2B, n3B = alunos[matr2][2]
  n1 = n1A + n2A + n3A
  n2 = n1B + n2B + n3B
  
  if n1 + verificaBonus(n1, alunos[matr1][3]) > n2 + verificaBonus(n2, alunos[matr2][3]): 
    return True # desempate por nota com bônus

  if n1 + verificaBonus(n1, alunos[matr1][3]) == n2 + verificaBonus(n2, alunos[matr2][3]):
    # desempate por nota sem bônus
    if n1>n2: 
      return True 
    elif n1 == n2: # desempate por semestre letivo
      a1, s1 = alunos[matr1][1]
      a2, s2 = alunos[matr2][1]
      
      # verifica o ano mais recente
      if a1 > a2:
        return True
      elif a1 == a2:
        # verifica o semestre mais recente 
        if s1 > s2: 
          return True
        elif s1 == s2:
          # desempate por ordem alfabética
          if alunos[matr1][0] < alunos[matr2][0]: return True
          elif alunos[matr1][0] == alunos[matr2][0]:
            # desempate por matrícula
            if matr1 > matr2: return True
  return False


# verifica qual o bônus do aluno baseado em sua nota e quantidade de faltas
def verificaBonus(total, faltas):
  if faltas == 0 and total != 100:
    if total == 99:
      return 1
    return 2
  return 0

# busca binaria que verifica a quantidade de alunos com nota maior ou igual a x
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

# função responsável por imprimir na tela o número de alunos aprovados pelo professor
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
  print(len(alunosApr))


def saida(lMatricula, alunos):
  # abre o arquivo para escrita
  with open('saida.txt', 'w', encoding='utf-8') as f:
    
    # escreve no arquivo os dados de cada aluno
    for matr in lMatricula:
      nome, _, notas, faltas = alunos[matr]
      n1, n2, n3 = notas
      total = n1 + n2 + n3

      # imprime o bonus, caso exista
      if verificaBonus(total, faltas) != 0:
        f.write(f'{nome} - {total} +{verificaBonus(total, faltas)}\n')
      else:
        f.write(f'{nome} - {total}\n')
        
  return 0


# leitura do arquivo binário e retorna dicionário com os dados
def readArq():
  arquivo = 'entrada100000.bin'

  # verifica se o arquivo existe
  if os.path.isfile(arquivo):
    # abre o arquivo para leitura e gera um dicionario com os dados
    with open(arquivo, 'rb') as arq:
      dic = pickle.load(arq) 
    return dic

# programa principal
def main():
  alunos = readArq()
  matr = ordenaAlunos(alunos)
  saida(matr, alunos)
  verificaAprovados(matr, alunos)
  
  #c.compararSaidas('saida.txt', 'saida100000.txt')
  
  return 0


if __name__ == '__main__':
  main()