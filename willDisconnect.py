"""
You are not allowed to import anything.
"""

def willDisconnect(G, e):
    """
    First remove e from G
    """
    neighbours = G[e[0]] 
    for v in neighbours:
        if v == e[1]:
            neighbours.remove(e[1]) 
            break
    
    G[e[0]] = neighbours

    """
    Initialize a set S to e[0]
    """
    S = set()
    S.add(e[0])

    """
    Keep augmenting S with neighbours till we cannot any longer
    """
    
    while True:
        copyS = S.copy() 
        for u in copyS:
            """
            add all neighbours of u to S
            """
            vertices = G[u] 
            S.update(vertices) 
        
        """
        Now check if copyS and S are the same, i.e., nothing changed
        If yes, break
        """
        if copyS == S:
            break

    """
    Finally check if e[1] is in S and return True/False as appropriate
    """
   
    for elem in S:
        if elem == e[1]:
            return False

    return True
