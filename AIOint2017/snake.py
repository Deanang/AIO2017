I, O = open('snakein.txt', 'r'), open('snakeout.txt', 'w')
x, y = [int(x) for x in I.readline().split()]

class Snake(object):
    def __init__(self):
        #Initialize the 4 attributes of a snake, i.e (x, y), face and dist.
        self.x = 0
        self.y = 0
        self.face = 'N'
        self.dist = abs(self.x-x)+abs(self.y-y)
    #Method to calculate the Mahattan dist of the point on the left
    def leftDist(self):
        a, b = self.x, self.y
        if self.face == 'N':
            a -= 1
        elif self.face == 'E':
            b -= 1
        elif self.face == 'S':
            a += 1
        else:
            b += 1
        return abs(x-a)+abs(y-b)
    #Method to calculate the Mahattan dist of the point on the right
    def rightDist(self):
        a, b = self.x, self.y
        if self.face == 'N':
            a += 1
        elif self.face == 'E':
            b += 1
        elif self.face == 'S':
            a -= 1
        else:
            b -= 1
        return abs(x-a)+abs(y-b)
    def moveLeft(self):
        F = ['N', 'E', 'S', 'W']
        i = F.index(self.face)
        if self.face == 'N':
            self.x -= 1
        elif self.face == 'E':
            self.y -= 1
        elif self.face == 'S':
            self.x += 1
        else:
            self.y += 1
        self.dist = abs(self.x-x)+abs(self.y-y)
        self.face = F[(i+1)%4]
    def moveRight(self):
        F = ['N', 'E', 'S', 'W']
        i = F.index(self.face)
        if self.face == 'N':
            self.x += 1
        elif self.face == 'E':
            self.y += 1
        elif self.face == 'S':
            self.x -= 1
        else:
            self.y -= 1
        self.dist = abs(self.x-x)+abs(self.y-y)
        self.face = F[(i-1)%4]

ans = ''
Dean = Snake()
while(Dean.dist != 0):
    if Dean.leftDist() <= Dean.rightDist():
        Dean.moveLeft()
        ans += 'L'
    else:
        Dean.moveRight()
        ans += 'R'
O.write(str(ans))
