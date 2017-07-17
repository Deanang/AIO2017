with open('addin.txt', 'r') as I:
    a, b = [int(x) for x in I.readline().split()]
I.close()
print(a, b)

with open('addout.txt', 'w') as O:
    O.write(str(a+b))
O.close()
