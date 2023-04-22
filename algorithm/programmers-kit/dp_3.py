def solution(m, n, puddles):
    state = [[0 for _ in range(m)] for _ in range(n)]
    state[0][0] = 1
    for col, row in puddles:
        state[row - 1][col - 1] = None
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                pass
            elif state[i][j] is None:
                state[i][j] = 0
            else:
                target = []
                if i > 0:
                    target.append(state[i - 1][j])
                if j > 0:
                    target.append(state[i][j - 1])
                state[i][j] = sum(target)
    answer = state[-1][-1]
    return answer % 1000000007