# DO NOT UPLOAD THIS FILE
def pop_wait(wait, now, sort=True):
    if sort:
        wait.sort(key=lambda x: x[1])
    call, time = wait.pop(0)
    after = now + time
    result = after - call
    return wait, after, result


def solution(jobs):
    jobs.sort()
    now = 0
    answer = 0
    wait = []
    for call, time in jobs:
        if call < now:
            wait.append((call, time))
        elif call == now:
            wait.append((call, time))
            wait, now, result = pop_wait(wait, now, sort=True)
            answer += result
        elif len(wait) == 0:
            now = call + time
            answer += time
        else:
            wait.sort(key=lambda x: x[1])
            while call > now:
                wait, now, result = pop_wait(wait, now, sort=False)
                answer += result
            wait.append((call, time))
            wait, now, result = pop_wait(wait, now, sort=True)
            answer += result
    wait.sort(key=lambda x: x[1])
    while len(wait) > 0:
        wait, now, result = pop_wait(wait, now, sort=False)
        answer += result
    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))
