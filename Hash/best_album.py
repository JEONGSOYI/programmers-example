## Python 2.7.15

def solution(genres, plays):
    genres_sum = {}
    genres_idx = {}
    for i,n in enumerate(plays):
        if genres[i] in genres_sum.keys():
            genres_sum[genres[i]] = genres_sum[genres[i]] + n
            if n in genres_idx[genres[i]].keys():
                genres_idx[genres[i]][n].append(i)
            else:
                genres_idx[genres[i]].update({n:[i]})
        else:
            genres_sum[genres[i]] = n
            genres_idx[genres[i]] = {n:[i]}
    key = genres_sum.keys()
    value = sorted(genres_sum.values(), reverse=True)
    answer = []
    for i in value:
        idx = genres_idx[key[genres_sum.values().index(i)]]
        tmp = sorted(idx, reverse=True)
        a = 0
        for j in tmp:
                b = sorted(idx[j])
                if len(b)>3:
                    answer = answer + b[0:2]
                    a = a + 2
                else:
                    answer = answer + b
                    a = a + len(b)
                if a==2:
                    break
    return answer

