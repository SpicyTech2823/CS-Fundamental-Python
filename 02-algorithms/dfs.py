def dfs(graph, current, visited=None):

    if visited is None:
        visited = set()

    # Mark current node as visited
    visited.add(current)

    print(current, end=" ")

    # Visit neighbors
    for neighbor in graph[current]:

        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Graph
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

dfs(graph, "A")