#undirected   
n=4
edges = [(1,2,2) , (2,3,1) , (4,3,1) , (1,4,1)]
adj={}
for i in range(1,n+1):
    adj[i]=[]
print(adj)
for i in edges:
    u,v,w=i
    adj[u].append((v,w))
    # adj[v].append(u)
print(adj)
print(adj[4])

def isNeighbour(adj):
    start = int(input())
    end = int(input())
    #start = 2 end = 4 ans = -1

    for i in adj[start]:
        if i[0] == end:
            return i[1]

    return -1

print(isNeighbour(adj))
