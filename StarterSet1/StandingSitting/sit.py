with open('sitin.txt', 'r') as inpt:
    r, s = [int(x) for x in inpt.readline().split()]
    tickets = int(inpt.readline())
    sit = r*s if r*s<=tickets else tickets
    stand = tickets-r*s if r*s<=tickets else 0
inpt.close()
with open('sitout.txt', 'w') as otpt:
    otpt.write(str(sit)+' '+str(stand))
otpt.close()
