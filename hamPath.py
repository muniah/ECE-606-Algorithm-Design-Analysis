
def hamPath(G):
    def dfs(path, visited):
        if len(path) == len(G):
            return path
        
        for neighbor in G[path[-1]]:
            if not visited[neighbor]:
                visited[neighbor] = True
                result = dfs(path + [neighbor], visited)
                if result:
                    return result
                visited[neighbor] = False
        
        return None

    for start in range(len(G)):
        visited = [False] * len(G)
        visited[start] = True
        result = dfs([start], visited)
        if result:
            return result
    
    return None


