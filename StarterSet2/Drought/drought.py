with open('rainin.txt', 'r') as I:
    n, c = [int(x) for x in I.readline().split()]
    sum = 0
    with open('rainout.txt', 'w') as O:
        for i in range(n):
            sum += int(I.readline())
            if sum >= c:
                O.write(str(i+1))
                break
    O.close()
I.close()
