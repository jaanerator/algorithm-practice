from math import sqrt


def solution(brown, yellow):
    size = brown + yellow
    for h in range(3, int(sqrt(size)) + 1):
        if size % h == 0:
            w = size / h
            if (w - 2) * (h - 2) == yellow:
                answer = [w, h]
    return answer