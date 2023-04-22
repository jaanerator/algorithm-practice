def solution(sizes):
    size_min = []
    size_max = []
    for size in sizes:
        size_min.append(min(size))
        size_max.append(max(size))
    
    answer = max(size_min) * max(size_max)
    return answer