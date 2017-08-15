#Files I/O
I = open('chairsin.txt', 'r'), O = open('chairsout.txt', 'w')
#Read values of C - No. of chairs, N -No. of friends and K - No.of friends who can sit wet or dry.
C, N, K = [int(x) for x in I.readline().split()]
#Read the state of the chairs (wet or dry)
L = I.readline().strip()
#P is the number of friends who can only sit on dry chairs.
P = N - K
#A is a list of the indices of the dry chairs in L
A = [i for i in range(len(L)) if L[i]=='d']
#If no friend is 'picky', then return N as the short block length
if P == 0:
    ans = N
# If there is at least a picky friends, sit this group first.
else:
    #B stores the list of elements in A that are P elements apart.
    B = [A[i+P-1]-A[i]+1 for i in range(len(A)-P+1)]
    #min(B) minimises the required block length
    #After sitting the P friends, now sit the remaining K friends.
    #If min(B) is longer than N, then answer is min(B)
    #Else it's just N
    ans = max(N, min(B))
#print(ans)
O.write(str(ans))
