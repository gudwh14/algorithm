# v: 정점, discovered : 방문했던 정점
def recursive_dfs(v, discovered=[]) -> []:
    discovered.append(v)
    for adjacent in graph[v]:
        if adjacent not in discovered:
            discovered = recursive_dfs(adjacent, discovered)
    return discovered


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

print(recursive_dfs(1))
