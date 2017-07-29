with open('dictin.txt', 'r') as I:
    d, w = [int(x) for x in I.readline().split()]
    D = dict()
    for i in range(d):
        a, b = [int(x) for x in I.readline().split()]
        D[a] = b
    with open('dictout.txt', 'w') as O:
        for j in range(w):
            i = int(I.readline())
            if i in D:
                O.write(str(D[i])+'\n')
            else:
                O.write('C?'+'\n')
    O.close()
I.close()
