from collections import defaultdict, deque

# -----------------------
# Topological Sort (Kahn's Algorithm)
# -----------------------
def topological_sort(vertices, edges):
    graph = defaultdict(list)
    in_degree = {v: 0 for v in vertices}

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([v for v in vertices if in_degree[v] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order if len(topo_order) == len(vertices) else None


# -----------------------
# Depth-First Search (DFS)
# -----------------------
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


# -----------------------
# Kruskal's Algorithm (MST)
# -----------------------
def kruskal(n, edges):
    parent = list(range(n))

    def find(u):
        while u != parent[u]:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        root_u, root_v = find(u), find(v)
        if root_u == root_v:
            return False
        parent[root_v] = root_u
        return True

    mst = []
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if union(u, v):
            mst.append((u, v, weight))

    return mst


# -----------------------
# TEST CASES
# -----------------------
def run_tests():
    print("\n--- Topological Sort Test (CLRS-style 'getting dressed') ---")
    vertices = ['undershorts', 'pants', 'belt', 'shirt', 'tie', 'jacket', 'socks', 'shoes', 'watch']
    edges = [('undershorts', 'pants'), ('undershorts', 'shoes'), ('pants', 'belt'),
             ('belt', 'jacket'), ('shirt', 'belt'), ('shirt', 'tie'),
             ('tie', 'jacket'), ('socks', 'shoes')]
    topo_result = topological_sort(vertices, edges)
    print("Topological Order:", topo_result)

    print("\n--- DFS Test (CLRS Figure 22.6 Directed Graph) ---")
    graph = {
        'u': ['v', 'x'],
        'v': ['y'],
        'w': ['y', 'z'],
        'x': ['v'],
        'y': ['x'],
        'z': ['z']
    }
    dfs_result = dfs(graph, 'u')
    print("DFS Visited Nodes from 'u':", dfs_result)

    print("\n--- Kruskal's Algorithm Test (CLRS Figure 23.4 MST) ---")
    n = 9  # vertices 0 to 8
    edges = [
        (0, 1, 4), (0, 7, 8),
        (1, 2, 8), (1, 7, 11),
        (2, 3, 7), (2, 8, 2), (2, 5, 4),
        (3, 4, 9), (3, 5, 14),
        (4, 5, 10),
        (5, 6, 2),
        (6, 7, 1), (6, 8, 6),
        (7, 8, 7)
    ]
    mst_result = kruskal(n, edges)
    print("Edges in MST:")
    for u, v, w in mst_result:
        print(f"{u} - {v} : {w}")
    total_weight = sum(w for _, _, w in mst_result)
    print("Total Weight:", total_weight)

# Run all tests
if __name__ == "__main__":
    run_tests()
