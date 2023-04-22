def get_first_digit(number, k):
    num_list = [char for char in number[:k + 1]]
    start_idx = num_list.index(max(num_list))
    return start_idx


def solution(number, k):
    answer = ''
    while k > 0:
        start_idx = get_first_digit(number, k)
        answer += number[start_idx]
        number = number[start_idx + 1:]
        k -= start_idx
    answer += number
    return answer