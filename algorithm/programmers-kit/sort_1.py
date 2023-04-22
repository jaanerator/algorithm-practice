def solution(array, commands):
    answer = []
    for i, j, k in commands:
        array_sub = array[i - 1:j]
        array_sub.sort()
        answer.append(array_sub[k - 1])
    return answer