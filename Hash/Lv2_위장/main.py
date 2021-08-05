def solution(clothes):
    types = []
    for _, type in clothes:
        types.append(type)

    clothe_info = {}
    for t in types:
        names = 0
        for _, type in clothes:
            if t == type:
                names += 1
        clothe_info[t] = names

    answer = 1
    for v in clothe_info.values():
        answer *= (v + 1)
    answer = answer - 1

    return answer
