with open('countin.txt', 'r') as I:
    n = int(I.readline())
I.close()

with open('countout.txt', 'w') as O:
    for i in range(n):
        O.write(str(i+1)+'\n')
O.close()
