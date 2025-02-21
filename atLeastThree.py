def atLeastThree(G, u, v):
    paths = list()
    queue = list()

    path = [u]
    queue.append(path.copy())
    
    while queue:
        path = queue.pop(0)
        last = path[len(path) - 1]
        if (last == v):
            paths.append(path)
            if len(paths) == 3:
                return paths
        
        for i in range(len(G[last])):
            if G[last][i] not in path:
                curr_path = path.copy()
                curr_path.append(G[last][i])
                queue.append(curr_path)
    return None

