I = open('snapin.txt', 'r')
O = open('snapout.txt', 'w')

R, C, rrose, crose, rscarlet, cscarlet = [int(x) for x in I.readline().split()]
#print(R, C, rrose, crose, rscarlet, cscarlet)
ans = 'SCARLET' if (rrose+crose)%2 == (rscarlet+cscarlet)%2 else 'ROSE'
#print(ans)

O.write(ans)
