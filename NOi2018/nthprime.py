n=30
mx = 10*n
def nthprime(n):
    P = [0,0]+[1]*(mx-2)
    for i in range(2, mx):
        if P[i]==1:
            if n == 1:
                return i
            else:
                n -= 1
                for j in range(2*i, mx, i):
                    P[j] = 0
print(nthprime(n))
