def make_graph(costs):
    graph = {}
    for node_i, node_j, _ in costs:
        registered_nodes = graph.keys()
        if node_i not in registered_nodes:
            graph[node_i] = [node_j]
        else:
            graph[node_i].append(node_j)
        if node_j not in registered_nodes:
            graph[node_j] = [node_i]
        else:
            graph[node_j].append(node_i)
    return graph


def bfs(node, graph, n):
    visited = [False] * n
    visited[node] = True
    queue = graph[node]
    while len(queue) > 0:
        next_node = queue.pop(0)
        visited[next_node] = True
        queue += [neighbor for neighbor in graph[next_node]
                  if not visited[neighbor] and neighbor not in queue]
    return visited


def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    real_costs = []
    visited = [False] * n
    while not all(visited):
        real_costs.append(costs.pop(0))
        graph = make_graph(real_costs)
        visited = bfs(list(graph.keys())[0], graph, n)
    answer = sum([cost[2] for cost in real_costs])
    return answer