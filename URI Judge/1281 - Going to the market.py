import string


n = int(input().strip())


for i in range(n):
    fruta = {}
    fruta2 = {}
    m = int(input().strip())
    z = 0
    for i in range(m):
        temp1, temp2 = (input().strip()).split()
        temp1 = str(temp1)
        temp2 = float(temp2)
        fruta.update({temp1: temp2})

    p = int(input().strip())
    while p < 1 or p > m:
        print("Valor invalido")
        p = int(input().strip())
    for i in range(p):
        temp1, temp2 = (input().strip()).split()
        temp1 = str(temp1)
        if len(temp1) > 50:
            print("Valor invalido")
            break
        temp2 = int(temp2)
        fruta2.update({temp1: temp2})

    for item in fruta2:
        x = fruta.get(item)
        y = fruta2.get(item)
        z = z + x * y
    print("R$", "%.2f" % z)
