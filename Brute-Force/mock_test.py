## python 3.5.6

def solution(answers):
    ans = []
    x1 = [1, 2, 3, 4, 5] * int(10000/5)
    x2 = [2, 1, 2, 3, 2, 4, 2, 5] * int(10000/8)
    x3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * int(10000/10)

    x1 = x1[0:len(answers)]
    x2 = x2[0:len(answers)]
    x3 = x3[0:len(answers)]

    s = [sum(map(lambda x: x[0]==x[1], zip(answers, x1))),
        sum(map(lambda x: x[0]==x[1], zip(answers, x2))),
        sum(map(lambda x: x[0]==x[1], zip(answers, x3)))]

    for i,x in enumerate(s):
        if x==max(s) :
            ans.append(i+1)
    return ans

