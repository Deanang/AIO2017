with open("manin.txt", "r") as I:
    Ix, Cx, Id, Cd = (int(x) for x in I.readline().split())

with open("manout.txt", "w") as O:
    O.write(str(Ix+Id) if Ix+Id in (Cx+Cd, Cx-Cd) else str(Ix-Id))
