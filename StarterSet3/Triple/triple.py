with open('tripin.txt', 'r') as I:
    n = int(I.readline())
    trip = []
    for i in range(1, n+1):
        if int(I.readline()) % 3 == 0:
            trip += [i]

with open('tripout.txt', 'w') as O:
    if trip == []:
        O.write("Nothing here!")
    else:
        O.write(str(len(trip))+'\n')
        for x in trip:
            O.write(str(x)+' ')
