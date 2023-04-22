from itertools import permutations
from math import sqrt


def is_prime(num):
    if num in [0, 1]:
        result = False
    elif num in [2, 3]:
        result = True
    else:
        result = True
        for i in range(2, int(sqrt(num)) + 1):
            if num // i * i == num:
                result = False
                break
    return result


def solution(numbers):
    perm = []
    for i in range(1, len(numbers) + 1):
        perm += list(permutations(numbers, i))
    answer = []
    for number in perm:
        number = int(''.join(list(number)))
        if number in answer:
            pass
        elif is_prime(number):
            answer.append(number)
        else:
            pass
    return len(answer)
