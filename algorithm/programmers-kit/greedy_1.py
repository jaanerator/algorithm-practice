def solution(n, lost, reserve):
    reserve_new = []
    for res in reserve:
        if res in lost:
            lost.pop(lost.index(res))
        else:
            reserve_new.append(res)
    
    std_los = [False] * (n + 2)
    std_res = [False] * (n + 2)
    for los in lost:
        std_los[los] = True
    for res in reserve_new:
        std_res[res] = True
    
    for i in range(1, n + 1):
        if not std_los[i]:
            pass
        elif std_res[i - 1]:
            std_los[i] = False
            std_res[i - 1] = False
        elif std_res[i + 1]:
            std_los[i] = False
            std_res[i + 1] = False
        else:
            pass
    answer = n - sum(std_los)
    return answer