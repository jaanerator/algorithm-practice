def solution(operations):
    hq = []
    for oper in operations:
        command, num = oper.split()
        if command == 'I':
            hq.append(int(num))
        elif len(hq) == 0:
            pass
        elif num == '1':
            hq.sort()
            hq.pop(-1)
        else:
            hq.sort()
            hq.pop(0)
        print(hq)
    
    if len(hq) == 0:
        answer = [0, 0]
    else:
        answer = [max(hq), min(hq)]
    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
