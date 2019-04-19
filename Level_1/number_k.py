# Python3.7.1
# 19/04/12

def solution(array, commands):
    answer = []
    for idx in commands:
        i = idx[0]
        j = idx[1]
        k = idx[2]
        tmp = sorted(array[(i-1):j])
        answer += [tmp[k-1]]
    return answer
