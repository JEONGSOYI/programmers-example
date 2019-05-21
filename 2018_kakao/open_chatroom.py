## python 2.7
## 19/05/21
## https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    nick = {}
    array = []
    for s in record:
        sp = s.split(' ')
        if sp[0]=="Enter":
            nick[sp[1]] = sp[2]
            array.append([sp[1], "님이 들어왔습니다."])
        elif sp[0]=="Leave":
            array.append([sp[1], "님이 나갔습니다."])
        else:	# "Change"
            nick[sp[1]] = sp[2]
    answer = map(lambda x: nick[x[0]] + x[1], array)
    return(answer)

