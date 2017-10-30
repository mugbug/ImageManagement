matrix = []

print('Entre com uma matriz para comprimir ou pressione enter para usar uma matriz default:')
# input example:
# 4
# 0 1 1 0
# 0 1 1 1
# 0 0 0 1
# 0 1 0 1

nRow = input('Numero de linhas da matriz:')
if nRow != '':
    nRow = int(nRow)
    for i in range(nRow):
        row = [int(x) for x in input().split()]
        matrix.append(row)

if matrix == [] or nRow == '':
    matrix = [
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]

r = len(matrix)
c = len(matrix[0])

RLE = [[] for i in range (r)]

for i in range(r):
    previous = matrix[i][0]
    count = 0
    for j in range(c):

        # primeira coluna é preta
        if j == 0 and matrix[i][j] == 0:
            RLE[i].append(0)

        # se nao mudou de cor, incrementa count
        if previous == matrix[i][j]:
            count += 1

        # se mudou de cor, adiciona à linha
        elif previous != matrix[i][j]:
            RLE[i].append(count)
            count=1
        
        # se chegou ao final da linha, adiciona à linha
        if j == (c-1):
            RLE[i].append(count)
        previous = matrix[i][j]

print('Matriz original:   {}\nMatriz comprimida: {}'.format(matrix, RLE))