with open('mixin.txt', 'r+') as f:
    n,d = [int(x) for x in f.readline().split()]
    # n is the numerator, d is the denominator
    a = n//d
    b = str(n%d)+'/'+str(d) if n%d != 0 else ''


with open('mixout.txt', 'w+') as f:
    f.write('%d %s' % (a, b))
