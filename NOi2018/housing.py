n=20
def m(n, k):
    return 0 if n<k else 1 + sum([m(n-i, i) for i in range(k, n//2+1)])
