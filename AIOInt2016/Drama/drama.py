import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Farmer Drama
#
# Australian Informatics Olympiad 2016
#
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# MAX_N is the largest possible number of plots on the farm, as defined in the
# problem statement.
MAX_N = 100000

# $(N)s is the number of plots on the farm
N = None

# plots, is an array of integers representing the sizes of the plots of land.
plots = [None for x in range(MAX_N + 3)]

# Open the input and output files.
input_file = open('farmin.txt', 'r')
output_file = open("farmout.txt", "w")

# Read the value of N from the input file.
N = int(input_file.readline().strip())

# Read in the array describing the plots.
input_line = input_file.readline().strip()
plots = list(map(int, input_line.split()))

# TODO: This is where you should compute your solution and store it into the
ans = 0
if len(plots)>1:
    keep, destroy = 0, 0
    leftSum, rightSum = plots.pop(0), plots.pop()
    while plots:
        #print(W, leftSum, rightSum, keep, destroy)
        if leftSum == rightSum:
            keep += 2
            if len(plots)==1:
                keep += 1
                break
            else:
                leftSum += plots.pop(0)
                rightSum += plots.pop()
        elif leftSum > rightSum:
            destroy += 1
            rightSum += plots.pop()
        else:
            destroy += 1
            leftSum += plots.pop(0)
        #print(W, leftSum, rightSum, keep, destroy)
    ans = destroy + (leftSum != rightSum)

# Write the answer to the output file.
output_file.write("%d\n" % (ans))

# Finally, close the input/output files.
input_file.close()
output_file.close()
