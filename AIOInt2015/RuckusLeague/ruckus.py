I, O = open('ruckusin.txt', 'r'), open('ruckusout.txt', 'w')
N, L, K, M = [int(x) for x in I.readline().split()]
#print(N, L, K, M)

for i in range(L):
    a, b  = [int(x) for x in I.readline().split()]
    if  type(graph[a]) == list and type(graph[b]) == list:
        longer = a if len(graph[a])>=len(graph[b]) else b
        shorter = b if longer == a else a
        graph[longer] += graph[shorter]
        graph[shorter] = longer
    elif graph[a] == graph[b]:
        graph[graph[a]] += [graph[b]]
    else:
        isint = a if type(graph[a]) == int else b
        lst = b if isint == a else a
        if lst == graph[isint]:
            graph[lst] += [graph[isint]]
        else:
            graph[graph[isint]] += graph[lst]
            graph[lst] = graph[isint]

graph = [x for x in graph if type(x)==list]
print(graph)
