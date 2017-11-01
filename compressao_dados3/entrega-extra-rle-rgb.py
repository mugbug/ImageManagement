matrix = [
    [[0,0,0], [255,0,0], [123,132,0], [14,0,0]], 
    [[44,4,12], [0,12,0], [332,0,0], [14,0,0]],
    [[44,0,0], [123,0,0], [0,0,123], [0,0,123]],
    [[4,4,4], [4,4,4], [4,4,4], [44,12,0]]
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


# print('Matriz original:   {}\nMatriz comprimida: {}'.format(matrix, RLE))

print('Matriz original:')
for i in range(r):
    print(matrix[i])

print('Matriz compimida:')
for i in range(r):
    print(RLE[i])