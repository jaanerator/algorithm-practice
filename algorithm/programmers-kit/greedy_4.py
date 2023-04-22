def make_one_boat(ordered_people, limit):
    if len(ordered_people) == 1:
        return []
    else:
        person_max = ordered_people.pop(-1)
        if person_max + ordered_people[0] <= limit:
            person_min = ordered_people.pop(0)
            now_weight = person_max + person_min
            while len(ordered_people) > 0:
                if now_weight + ordered_people[0] > limit:
                    break
                else:
                    now_weight += ordered_people.pop(0)
        return ordered_people
    

def solution(people, limit):
    people.sort()
    answer = 0
    while len(people) > 0:
        people = make_one_boat(people, limit)
        answer += 1
    return answer