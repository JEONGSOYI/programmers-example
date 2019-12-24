## 19/04/05
## Python 3.7.1

def solution(phone_book):
    answer = True
    x = list(set(phone_book))
    x.sort()
    for idx,value in enumerate(x):
        y = x[(idx+1):len(x)]
        for i in range(len(y)):
            if value in y[i]:
                return False
    return(answer)

