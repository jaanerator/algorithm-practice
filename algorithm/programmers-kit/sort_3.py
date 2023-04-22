def solution(citations):
    citations.sort(reverse=True)
    answer = min(citations[-1], len(citations))
    for i in range(len(citations)):
        h = i + 1
        cite_min = citations[i]
        if h > cite_min:
            answer = h - 1
            break
    return answer