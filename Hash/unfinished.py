## 19/04/05
## Python 3.7.1

def solution(participant, completion):
	participant.sort()
	completion.sort()
	if len(set(participant))==len(set(completion)):
		for i in range(len(completion)):
			if completion[i]!=participant[i]:
				return(participant[i])
	else:
		tmp = list(set(participant) - set(completion))
		return(tmp[0])

