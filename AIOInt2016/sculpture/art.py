I = open("artin.txt", "r")
O = open("artout.txt", "w")

N = int(I.readline()) #Read input line by line
D = [int(x) for x in I.read().split()] #Reading all data at once
#Split the data into time, width and height lists(arrays)
T = [D[i] for i in range(0, len(D), 3)]
W = [D[i] for i in range(1, len(D), 3)]
H = [D[i] for i in range(2, len(D), 3)]

ans = H[0]
stackHeight = [H[0]]
extension = [T[0]+W[0]-1]
for i in range(1, N):
    #Check the next available platform level if there is a drop.
    while extension!=[] and T[i] > extension[-1]:
        #Discard most recent extension and stackHeight info if T[i] is greater.
        extension.pop()
        stackHeight.pop()
    #Out of the while loop, we have found a platform level to catch the dropping block.
    #Re-accumulate the height of the stack
    if extension:
        stackHeight.append(stackHeight[-1]+H[i])
    #Here, none of the extension catches the block.
    #It drops to the ground and we start again.
    else:
        stackHeight.append(H[i])
    #ans keep tracks of the maximum of all stack heights.
    ans = max(ans, stackHeight[-1])
    #Append the next extension after the block dropped.
    extension.append(T[i]+W[i]-1)

print(ans)
O.write(str(ans))

I.close()
O.close()
