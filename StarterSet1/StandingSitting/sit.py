with open("sitin.txt", "r") as I:
    r, s = [int(x) for x in I.readline().split()]
    tickets = int(I.readline())
    sit = r*s if r*s<=tickets else tickets
    stand = tickets-r*s if r*s<=tickets else 0
I.close()

with open('sitout.txt', 'w') as O:
    O.write(str(sit)+' '+str(stand))
O.close()
