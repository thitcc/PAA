visited = []


def dfs(u):

    visited[ u ] = True
    for v in graph[ u ]:
        if not visited[ v ]:
            dfs(v)