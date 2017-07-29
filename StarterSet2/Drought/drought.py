with open('rainin.txt', 'r') as I:
    n, c = [int(x) for x in I.readline().split()]
    print(n, c)
I.close()




with open('rainout.txt', 'w') as O:
    pass
O.close()
