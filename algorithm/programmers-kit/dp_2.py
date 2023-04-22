def solution(triangle):
    for i in range(1, len(triangle)):
        row = triangle[i]
        for j in range(len(row)):
            now = row[j]
            target = []
            if j - 1 >= 0:
                target.append(now + triangle[i - 1][j - 1])
            if j < i:
                target.append(now + triangle[i - 1][j])
            triangle[i][j] = max(target)
    return max(triangle[-1])