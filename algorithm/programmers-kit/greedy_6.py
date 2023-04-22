def solution(routes):
    routes.sort()
    answer = 1
    m = 30000
    for in_pts, out_pts in routes:
        if in_pts > m:
            answer += 1
            m = out_pts
        else:
            m = min(m, out_pts)
    return answer