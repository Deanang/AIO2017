with open("chimin.txt", "r") as I:
    N = int(I.readline())
    S, T, X = I.readline(), I.readline(), I.readline()
numOfFlips = lambda A: sum(A[i]!=A[i-1] for i in range(1,len(A)))

A, ans = [0]*N, "SUCCESS"
for i in range(N):
    if not X[i] in (S[i], T[i]): ans = "PLAN FOILED";break
    elif X[i] == T[i] and S[i] != T[i]: A[i] = 1
    elif S[i] == T[i]: A[i] = A[i-1]

A = [A[i] for i in range(N) if S[i]!=T[i]]
if ans == "SUCCESS":  ans += "\n"+str(numOfFlips(A))

with open("chimout.txt", "w") as O:
    O.write(ans)
