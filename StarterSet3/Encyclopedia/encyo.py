with open('encyin.txt', 'r') as I:
    n, q = [int(x) for x in I.readline().split()]
    p = [None]*n
    for i in range(n):
        p[i]=int(I.readline())
    with open('encyout.txt', 'w') as O:
        for j in range(q):
            idx = int(I.readline()) - 1
            O.write(str(p[idx])+'\n')
    O.close()
I.close()
