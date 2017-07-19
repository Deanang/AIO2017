with open('bendin.txt','r') as K:
    x1, y1, x2, y2 = [int(x) for x in K.readline().split()]
    x3, y3, x4, y4 = [int(x) for x in K.readline().split()]
K.close()

A1 = (x2-x1)*(y2-y1)
A2 = (x4-x3)*(y4-y3)
Ox = (x2>=x3)*(min(x2,x4)-max(x1,x3))
Oy = (y2>=y3)*(min(y2,y4)-max(y1,y3))

with open('bendout.txt', 'w') as J:
    J.write(str(A1+A2-Ox*Oy))
J.close()
