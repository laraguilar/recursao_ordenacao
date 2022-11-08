'''
Trabalho Prático
Recursão e Ordenação
Disciplina: Programação II
Professor: Hilário Seibel
Grupo: Gabriely Moro e Lara Aguilar
'''

import pickle
import os





def readArq():
  arq = 'entrada10.bin'
  if os.path.isfile(arq):
    with open('entrada10.bin', 'rb') as arq:
      dic = pickle.load(arq)
    return dic
    


def main():
  print(readArq())
  return 0

if __name__ == '__main__':
  main()