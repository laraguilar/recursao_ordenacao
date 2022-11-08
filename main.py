'''
Trabalho Prático
Recursão e Ordenação
Disciplina: Programação II
Professor: Hilário Seibel
Grupo: Gabriely Moro e Lara Aguilar
'''

import pickle
import os


def saida(lMatricula, alunos):
  for matr in lMatricula:
    nome, _, notas, faltas = alunos[matr]
    n1, n2, n3 = notas
    total = n1 + n2 + n3
    if(faltas == 0 and total <= 98):
      print(f'{nome} - {total} +2')
    elif(total == 99):
      print(f'{nome} - {total} +1')
    else:
      print(f'{nome} - {total}')
  return 0
  
def ordenaAlunos(alunos):
  matr = []
  return matr

# leitura do arquivo binário e retorna dicionário com os dados
def readArq():
  arquivo = 'entrada100.bin'
  if os.path.isfile(arquivo):
    with open(arquivo, 'rb') as arq:
      dic = pickle.load(arq)
    return dic

def main():
  alunos = readArq()
  alunos['123'] = ('Gabi', (2022, 2), (30, 30, 39), 0)
  print(alunos)
  matr = ['BSI0638305', 'BSI1198746', 'BSI0304097', 'BSI0965229', '123']
  saida(matr, alunos)
  
  return 0

if __name__ == '__main__':
  main()