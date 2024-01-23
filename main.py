q, r, x, y = 0, "-", 0, 0
check = [int(input()) for _ in range(2)]
a, b = max(check), min(check)
x2, x1, y2, y1 = 1, 0, 0, 1
def evklid():
    matrix =[]
    matx = []
    matx.append(str("q").ljust(6))
    matx.append(str("r").ljust(6))
    matx.append(str("x").ljust(6))
    matx.append(str("y").ljust(6))
    matx.append(str("a").ljust(6))
    matx.append(str("b").ljust(6))
    matx.append(str("x2").ljust(6))
    matx.append(str("x1").ljust(6))
    matx.append(str("y2").ljust(6))
    matx.append(str("y1").ljust(6))
    matrix.append(matx)
    return matrix
matrix = evklid()
def evklid(q, r, x, y, a, b, x2, x1, y2, y1, matrix):
    check = True
    while True:
        if b == 0:
            check = False
        mat = []
        mat.append(str(q).ljust(6))
        mat.append(str(r).ljust(6))
        mat.append(str(x).ljust(6))
        mat.append(str(y).ljust(6))
        mat.append(str(a).ljust(6))
        mat.append(str(b).ljust(6))
        mat.append(str(x2).ljust(6))
        mat.append(str(x1).ljust(6))
        mat.append(str(y2).ljust(6))
        mat.append(str(y1).ljust(6))
        if b != 0:
            q, r = (a//b), (a%b)

        x, y = (x2-q*x1), (y2-q*y1)
        a, b, x2, y2, x1, y1 = b, r, x1, y1, x, y


        matrix.append(mat)
        if check == False:
            return matrix


matrix = evklid(q, r, x, y, a, b, x2, x1, y2, y1, matrix)

for i in (matrix):
    print(*i, sep=" ")







