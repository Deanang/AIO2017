with open("gecko.txt", "r") as F:
    h, w = [int(x) for x in F.readline().split()]
    L_previous = [int(x) for x in F.readline().split()]
    if h == 1:
        print(max(L_previous))
    else:
        for i in range(1, h):
            L = [int(x) for x in F.readline().split()]
            for j in range(w):
                if j==0:
                    L[j]=max(L[0]+L_previous[0], L[0]+L_previous[1])
                elif 1<=j<w-1:
                    L[j]=max(L[j]+L_previous[j-1], L[j]+L_previous[j], L[j]+L_previous[j+1])
                else:
                    L[j]=max(L[j]+L_previous[j-1], L[j]+L_previous[j])
            L_previous = L
        print(max(L))
