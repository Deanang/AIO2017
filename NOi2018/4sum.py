#4SUM solution
with open('4sum.txt', 'r') as I:
    A, B, C, D = [], [], [], []
    [na, nb, nc, nd] = [int(x) for x in I.readline().split()]
    for i in range(na):
      A.append(int(I.readline()))
    for i in range(nb):
      B.append(int(I.readline()))
    for i in range(nc):
      C.append(int(I.readline()))
    for i in range(nd):
      D.append(int(I.readline()))
#print(A, B, C, D)
I.close()

#Process Data
G1 = {a+b:(a, b) for a in A for b in B}
G2 = {a+b:(a, b) for a in C for b in D}
#print(G1, G2)
E, F = {a+b for a in A for b in B}, {c+d for c in C for d in D}
#print(E, F)
E, F = list(E), list(F)
E.sort(), F.sort()
#print(E, F)
while(E[0]+F[-1]!=0):
    while E[0]+F[-1]<0:
        E.pop(0)
    while E[0]+F[-1]>0:
        F.pop()
print(G1[E[0]][0], G1[E[0]][1], G2[F[-1]][0], G2[F[-1]][1])
