def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths



keys = G.keys()
start = [None,0]

for k in keys:
    before = len(G[k])
    if before > start[1]:
        start = [k,before]

maxPath = []
for k in range(len(keys)):
    newPaths =  find_all_paths(G,start[0],keys[k])
    for path in newPaths:
        print len(path)
        if( len(path) >= len(maxPath)):
            maxPath = path
#maxPath = max(p for p in paths)
print maxPath
print len(maxPath)
