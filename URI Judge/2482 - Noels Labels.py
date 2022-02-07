import string


n = int(input().strip())
while n < 1 or n > 100:
    n = int(input("Number of translations").strip())

christamas = {}
pessoas = {}

for i in range(n):
    temp1 = input().strip()
    temp1 = str(temp1)
    temp2 = input().strip()
    temp2 = str(temp2)
    christamas.update({temp1: temp2})

m = int(input().strip())
while m < 1 or m > 100:
    m = int(input("Number of people").strip())
for i in range(m):
    temp1 = input().strip()
    temp1 = str(temp1)
    temp2 = input().strip()
    temp2 = str(temp2)
    pessoas.update({temp1: temp2})

for item in pessoas:
    x = pessoas.get(item)
    y = christamas.get(x)
    print(item)
    print(y)
    print()
