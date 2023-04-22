def get_updown_solution(name):
    answer = 0
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    return answer


def get_leftright_solution(name):
    answer = float('inf')
    text = name
    for i in range(len(name)):
        pre = text[:i]
        post = text[i + 1:]
        while pre.startswith('A') or post.endswith('A'):
            if pre.startswith('A'):
                pre = pre[1:]
            if post.endswith('A'):
                post = post[:-1]
        cand = min(len(pre) * 2 + len(post), len(post) * 2 + len(pre))
        if cand < answer:
            answer = cand
        text = text[-1] + text[:-1]
    return answer
    

def solution(name):
    answer = get_updown_solution(name)
    answer += get_leftright_solution(name)
    return answer
