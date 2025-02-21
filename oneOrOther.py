"""
You are not allowed to import anything.

However, you are free to define any subroutines you want to structure your code well.
"""

def oneOrOther(G):
    def dfs(start, visited):
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(G[node])
        return visited

    n = len(G)
    for u in range(n):
        for v in range(u + 1, n):
            reachable_from_u = dfs(u, set())
            reachable_from_v = dfs(v, set())
            if v not in reachable_from_u and u not in reachable_from_v:
                return False
    return True
