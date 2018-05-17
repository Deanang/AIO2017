with open("snakein.txt", "r") as I:
    x, y = (int(x) for x in I.readline().split())
    a, b, D, ans = 0, 0, "N", ""
    d = lambda a, b: abs(a-x)+abs(b-y)
    def left(x, y, D):
      if D == "N": return (x-1, y, "W")
      if D == "W": return (x, y-1, "S")
      if D == "S": return (x+1, y, "E")
      if D == "E": return (x, y+1, "N")
    def right(x, y, D):
      if D == "N": return (x+1, y, "E")
      if D == "W": return (x, y+1, "N")
      if D == "S": return (x-1, y, "W")
      if D == "E": return (x, y-1, "S")
    while(d(a, b)!=0):
        statusleft, statusright = left(a, b, D), right(a, b, D)
        if d(statusleft[0], statusleft[1]) < d(statusright[0], statusright[1]):
            ans += "L"
            a, b, D = left(a, b, D)
        else:
            ans += "R"
            a, b, D = right(a, b, D)

with open("snakeout.txt", "w") as O:
    O.write(ans)
