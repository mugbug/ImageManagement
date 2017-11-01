RLE = []

print('Entre com uma matriz para comprimir ou pressione enter para usar uma matriz default:')

nRow = input('Numero de linhas da matriz:')
if nRow != '':
    nRow = int(nRow)
    for i in range(nRow):
        row = [int(x) for x in input().split()]
        RLE.append(row)

if RLE == [] or nRow == '':
    RLE = [
        [0, 1, 1, 2],
        [0, 4],
        [1, 1, 2],
        [1, 2, 1],
        [4]
    ]

r = len(RLE)

matrix = [[] for i in range (r)]

for i in range(r):
    c = len(RLE[i])
    if RLE[i][0] == 0:
        previous = 0
        k=1
    else:
        previous = 1
        k=0
    for j in range(k,c):
        current = RLE[i][j]
        while current != 0:
            matrix[i].append(previous)
            current -= 1
        
        if previous == 1:
            previous = 0
        else:
            previous = 1

# print('Matriz comprimida:   {}\nMatriz original: {}'.format(RLE, matrix))

print('Matriz compimida:')
for i in range(r):
    print(RLE[i])

print('Matriz original:')
for i in range(r):
    print(matrix[i])
