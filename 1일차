def solution(m,n,h,w,drops):
    never =len(drops) +1
    grid =[[never] * n for _ in range(m)]
    for order,(r,c) in enumerate (drops, start =1 ):
        grid[r][c] = order
    best_time = -1 
    answer = [0,0]
    for row in range(m-h+1):#이게 매우 중요
        for col in range(n-w+1):
            first_rain = never
            for r in range(row,row+h):
                for c in range(col,col+w):
                    first_rain = min(first_rain,grid[r][c])#굳이 list append말고 바로 
            if first_rain > best_time:
                best_time = first_rain
                answer = [row,col]
    return answer

def soultion(m,n,h,w,drops):
    never = len(drops)+1
    grid = [[never]*n for _ in range(m)]
    for x,(s,c) in enumerate(drops):
        grid[s][c] = x
    best_time = -1 
    ans =[0,0] #여기에 index 저장
    for row in range(m-h+1):
        for col in range(n-w+1):
            f_rain = never
            for r in range(row,row+h):
                for c in range(col, col+2):
                    f_rain  = min(f_rain, grid[r][c])
            if f_rain > best_time:
                best_tim = f_rain
                answer = [row,col]
    return answer 







#다른 풀이법 -> 이게 사실 답 (시간 땜에)
from collections import deque 

def soultion(m,n,h,w,drops):
    never = len(drops) + 1
    grid = [[never] * n for _ in range(m)]
    for order,(r,c) in enumerate(drops,start =1): #요기도 중요
        grid[r][c] = order
    
    width = n-w +1 
    #가로 구간의 최솟값을 저장할 공간 마련
    row_min =[[0]*width for _ in range(m)]
    for r in range(m):
        q=deque()
        for c in range(n):
            #후보의 위치가 현재 구간안에 있는지 확인하는것 
            while q and q[0] <=c-w:
                q.popleft()
            while q and grid[r][q[-1]] >= grid[r][c]:
                q.pop()
            q.append(c)
            if c >= w - 1:
                start_col = c - w + 1
                row_min[r][start_col] = grid[r][q[0]]


#두번쨰 문제 
def solution(cost, hint):
    n= len(cost)
    def DFS(L, curr_sum):
        if L ==n:
            print("최종비용:" curr_sum)
            return 
        DFS(L+1, curr_sum + cost[L][0])
    DFS(0,0)
