with open('magicin.txt', 'r') as I:
    [a, b, c] = [int(x) for x in I.readline().split()]
I.close()

with open('magicout.txt', 'w') as O:
    O.write('{0} {1} {2}'.format(a, b, c)+'\n'+'{0} {1} {2}'.format(c, a, b)+'\n'+'{0} {1} {2}'.format(b, c, a))
O.close()
