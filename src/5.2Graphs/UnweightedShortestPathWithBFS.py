# Link: https://www.codespeedy.com/python-program-to-find-shortest-path-in-an-unweighted-graph/
# IsDone: 0
def bfs(graph, S, D):
    queue = [(S, [S])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == D:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest(graph, S, D):
    try:
        return next(bfs(graph, S, D))
    except StopIteration:
        return None



graph = {'1': set(['2', '3']),
         '2': set(['1', '5']),
         '3': set(['1', '4']),
         '4': set(['3','5']),
         '5': set(['2', '4'])}
print(shortest(graph, '1', '5'))
list(bfs(graph, '1', '5'))