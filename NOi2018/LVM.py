with open("LVM.txt", "r") as F:
    N = int(F.readline())
    I = [F.readline() for x in range(N)]
    R, S = 0, []
    i = 0
    while(i<len(I)):
        if I[i][:4]=="PUSH":
            S.append(int(I[i][5:-1]))
            i += 1
        elif I[i][:5]=="STORE":
            R = S.pop()
            i += 1
        elif I[i][:4]=="LOAD":
            S.append(R)
            i += 1
        elif I[i][:4]=="PLUS":
            S.append(S.pop()+S.pop())
            i += 1
        elif I[i][:5]=="TIMES":
            S.append(S.pop()*S.pop())
            i += 1
        elif I[i][:6]=="IFZERO":
            if S.pop() == 0:
                i = int(I[i][7:-1])
            else:
                i += 1
        else:
            print(S[-1])
            break
F.close()
