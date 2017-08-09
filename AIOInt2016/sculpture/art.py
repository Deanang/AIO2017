I = open("artin.txt", "r")
O = open("artout.txt", "w")

N = int(I.readline()) #Read input line by line
D = [int(x) for x in I.read().split()]
T = [D[i] for i in range(0, len(D), 3)]
W = [D[i] for i in range(1, len(D), 3)]
H = [D[i] for i in range(2, len(D), 3)]

ans = H[0]
SH = [H[0]]
L = [T[0]+W[0]-1]
for i in range(1, N):
    while L!=[] and T[i] > L[-1]:
        L.pop()
        SH.pop()
    if L:
        SH.append(SH[-1]+H[i])
    else:
        SH.append(H[i])
    ans = max(ans, SH[-1])
    print()
    L.append(T[i]+W[i]-1)

print(ans)
O.write(str(ans))

I.close()
O.close()
