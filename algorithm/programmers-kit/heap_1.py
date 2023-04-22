from heapq import heappush, heappop


def solution(scoville, K):
    scoville.sort()
    answer = 0
    while True:
        min_1 = heappop(scoville)
        if min_1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        else:
            answer += 1
            min_2 = heappop(scoville)
            new = min_1 + (min_2 * 2)
            heappush(scoville, new)
    return answer
