# Recursão e Ordenação
Este trabalho utiliza funções recursivas e método de ordenação aprendidos na disciplina de Programação 2 do cursos Bacharelado em Sistemas de Informação.

## Especificações
Dado uma planilha de notas contendo:

- A matrícula do aluno.
- O nome do aluno.
- O semestre letivo.
- A nota do aluno em cada uma das 3 avaliações (2 provas de 30 e 1 trabalho de 40).
- O número de faltas do aluno.

É feita uma leitura do arquivo binário com esses dados, colocando-os em um dicionário. 
O programa é responsável por escrever o arquivo "saida.txt" com o nome do aluno junto com sua nota total por ordem decrescente, ou seja, do maior para o menor, e também imprime a quantidade de alunos aprovados (nota maior ou igual a 
 pontos)
 
### Método de Ordenação
O método de ordenação escolhido foi o **Merge Sort**, devido a complexidade do algoritmo ser **O(n * log n)** no pior caso, economizando recursos computacionais que não seriam possíveis nos outros métodos como o QuickSort e Selection Sort com complexidade O(n²) no pior cenário.
Devido às necessidades do problema proposto, uma adaptação é feita no merge, para que os critérios de desampate sejam cumpridos caso a nota de dois alunos seja igual.

#### Critérios de Ordenação:
1) Nota total (da maior para a menor).
2) Em caso de empate, pela nota sem o bônus.
3) Em caso de novo empate, pelo semestre letivo (do mais recente para o mais
antigo).
4) Em caso de novo empate, em ordem alfabética do nome.
5) Caso ainda haja empate, em ordem crescente de matrícula (não existem duas
matrículas iguais).

### Busca binária
Também é utilizada uma busca binária, adaptada para o caso, a fim de contar quantos alunos estão acima da média (60 pontos). Este é impresso na execução do programa.

