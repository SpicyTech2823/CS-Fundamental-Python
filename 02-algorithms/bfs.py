from collections import deque


def bfs(graph, start):

    visited = set()

    queue = deque()

    # Start from the starting node
    queue.append(start)

    visited.add(start)

    while queue:

        # Remove first node
        current = queue.popleft()

        print(current, end=" ")

        # Visit neighbors
        for neighbor in graph[current]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)


# Graph
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

bfs(graph, "A")