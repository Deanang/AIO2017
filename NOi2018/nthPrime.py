N = 30
P = [1]*(N+1)
P[1]=2
for i in range(2, N+1):
    P[i] = P[i-1]+1
    for j in range(1, i):
        if P[i]%P[j]
