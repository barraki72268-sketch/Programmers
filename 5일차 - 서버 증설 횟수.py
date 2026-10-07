# act 를 올려두고 -> 그 시점이 되면 뻬면됨
# 그럼 dy 테이블에 미래시점을 만들어 두면 되겠네 

def solution(players,m,k):
    cnt = 0
    dy = [0] * (len(players)+k)
    act = 0
    for i,x in enumerate(players):
        act -=dy[i]
        need = x//m
        if need > act:
            add = need - act 
            act += add
            cnt += add
            dy[i+k] += add
        answer = cnt
    return answer