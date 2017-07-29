with open('listin.txt', 'r') as I:
    f = int(I.readline())
    F = {}
    for i in range(f):
        a, b = [int(x) for x in I.readline().split()]
        if a not in F:
            F[a] = 1
        else:
            F[a] += 1
        if b not in F:
            F[b] = 1
        else:
            F[b] += 1

with open('listout.txt', 'w') as O:
    M = max(F.values())
    A = [x for x in F.keys() if F[x] == M]
    A.sort()
    for x in A:
        O.write(str(x)+'\n')
O.close()
