## python 3.5.6

def solution(heights):
    answer = [0]*len(heights)
    for i in range(len(heights),0,-1):
        for j in range(i-1,0,-1):
            if heights[i-1] < heights[j-1]:
                answer[i-1]=j
                break

