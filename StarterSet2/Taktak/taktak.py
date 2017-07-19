with open('taktakin.txt') as I:
    n = int(I.readline())
    count = 0
    while (n%11 != 1):
        n *= 2
        count += 1
I.close()
with open('taktakout.txt', 'w+') as O:
    O.write('{} {}'.format(count, n))
