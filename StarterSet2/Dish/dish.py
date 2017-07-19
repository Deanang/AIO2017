with open('dishin.txt') as f:
    n = int(f.readline())
    d = [int(f.readline()) for x in range(n)]
    mn, mx = min(d), max(d)
    mean = sum(d)/len(d)

with open('dishout.txt', 'w+') as f:
    f.write('%d %d %d' % (mn, mx, mean))
