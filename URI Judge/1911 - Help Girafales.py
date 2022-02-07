import string

alunos = {}
d = 0
n = int(input().strip())
while n < 1 or n > 50:
    n = int(input("Number of students").strip())
for i in range(n):
    temp1, temp2 = (input().strip()).split()
    temp1 = str(temp1)
    temp2 = str(temp2)
    alunos.update({temp1: temp2})

while True:
    n = int(input().strip())
    while n < 0 or n > 50:
        n = int(input("Number of students").strip())
    if n == 0:
        break
    for i in range(n):
        temp1, temp2 = (input().strip()).split()
        temp1 = str(temp1)
        temp2 = str(temp2)
        if temp1 in alunos:
            x = alunos.get(temp1)
            if x != temp2:
                d = d + 1
        else:
            alunos.update({temp1: temp2})
    if d != 0:
        print(d)

    d = 0
