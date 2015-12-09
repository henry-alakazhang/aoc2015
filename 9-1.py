import sys

def edgeEq(e1, e2):
    if (e1 == e2):
        return True
    if (e1[0] == e2[1] and e2[0] == e1[1]):
        return True
    return False

# store graph in an edges format
nodes = []
edges = {}

for line in sys.stdin:
    if line == '\n':
        break
    words = line.rstrip().split(' ')
    if words[0] not in nodes:
        nodes.append(words[0])
    if words[2] not in nodes:
        nodes.append(words[2])
    edges[(words[0],words[2])] = int(words[4])
    edges[(words[2],words[0])] = int(words[4])
        
# kruskal's algorithm with limiting factor
path = [] # path of nodes of 
visited = {node : 0 for node in iter(nodes)}
while len(path) < len(nodes) - 1:
    min = 100000
    next = ('','')
    for edge in iter(edges):
        visited[edge[0]] += 1
        visited[edge[1]] += 1
        ok = False
        for node in iter(visited):
            if visited[node] == 1:
                ok = True
        visited[edge[0]] -= 1
        visited[edge[1]] -= 1
        if (visited[edge[0]] > 1 or visited[edge[1]] > 1): # must be a path
            ok = False
        for pEdge in path: # check already in
            if (edgeEq(edge,pEdge)):
                ok = False
        if not ok:
            continue
        if edges[edge] < min:
            min = edges[edge]
            next = edge
    visited[next[0]] += 1
    visited[next[1]] += 1
    path.append(next)
    print(path)
    
sum = 0
print(path)
for edge in path:
    sum += edges[edge]
    
print(sum)