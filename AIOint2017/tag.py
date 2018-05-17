with open("tagin.txt", "r") as I:
    N, M = (int(x) for x in I.readline().split())
    R, B = set([1]), set([2])
    for i in range(M):
        X, Y = (int(x) for x in I.readline().split())
        SX = R if X in R else B
        SX.add(Y)

with open("tagout.txt", "w") as O:
    O.write("%s %s" % (len(R), len(B)))
