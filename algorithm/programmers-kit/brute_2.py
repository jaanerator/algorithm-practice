def solution(answers):
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    n_1 = len(pattern_1)
    n_2 = len(pattern_2)
    n_3 = len(pattern_3)
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        answer = answers[i]
        if answer == pattern_1[i % n_1]:
            cnt[0] += 1
        if answer == pattern_2[i % n_2]:
            cnt[1] += 1
        if answer == pattern_3[i % n_3]:
            cnt[2] += 1
    answer = [i + 1 for i, elem in enumerate(cnt) if elem == max(cnt)]
    return answer