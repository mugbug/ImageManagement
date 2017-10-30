matrix = []

print('Entre com uma matriz para comprimir ou pressione enter para usar uma matriz default:')

nRow = input('Numero de linhas da matriz:')
if nRow != '':
    nRow = int(nRow)
    for i in range(nRow):
        row = [int(x) for x in input().split()]
        matrix.append(row)

if matrix == [] or nRow == '':
    matrix = [
        [0,  255, 132, 14 ], 
        [44, 12,  332, 14 ],
        [44, 123, 123, 123],
        [4,  4,   44,  4  ],
        [1,  100, 100, 111]
    ]

r = len(matrix)
c = len(matrix[0])

RLE = [[] for i in range (r)]

for i in range(r):
    previous = matrix[i][0]
    count = 1
    for j in range(1,c):
        current = matrix[i][j]
        if previous != current:
            RLE[i].append(count)
            RLE[i].append(previous)
            count = 1
        else:
            count += 1
        if j == (c-1):
            RLE[i].append(count)
            RLE[i].append(current)
        previous = current


print('Matriz original:   {}\nMatriz comprimida: {}'.format(matrix, RLE))