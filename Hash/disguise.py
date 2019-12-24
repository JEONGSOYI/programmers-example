## Python 3.7.1

def solution(clothes):
    x = {}
    for i in clothes:
        if i[1] in x.keys():
            x[i[1]].append(i[0])
        else:
            x[i[1]] = [i[0]]
    key = x.keys()
    y = 1
    for i,n in enumerate(key):
        y = y * (len(x[n])+1)
    return(y-1)

