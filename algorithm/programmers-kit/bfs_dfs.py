# 여행경로
def solution(tickets):
    graph = {}
    for depart, arrive in tickets:
        if depart not in graph.keys():
            graph[depart] = [arrive]
        else:
            graph[depart].append(arrive)
    for value in graph.values():
        value.sort()
    
    answer = ['ICN']
    while any([len(value) > 0 for value in graph.values()]):
        answer.append(graph[answer[-1]].pop(0))
    return answer
