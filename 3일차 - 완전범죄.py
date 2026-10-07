#동적 계획법
def solution(info, n,m):
    INF = float("inf")
    dp =[INF] * m
    dp[0] = 0

    for a_trace , b_trace in info:
        next_dp = [INF] *m
        for b in range(m):
            if dp[b] == INF:
                continue
            new_a = dp[b] +a_trace
            if new_a < n:
                next_dp[b] = min(next_dp[b],new_a)
            new_b = b+ b_trace
            if new_b <m:
                next_dp[new_b] = min(next_dp[new_b],dp[b])
        dp = next_dp
    
    answer = min(dp)
    return -1 if answer == INF else answer


def solution(info,n,m):
    INF = float("inf")
    dp = [INF]*m
    dp[0] = 0
    for a_trace , b_trace in info:
        next_dp =[INF] * m 
        for b in range(m):
            if dp[b] == INF:
                continue
            new_a = dp[b] + a_trace 
            if new_a < n:
                next_dp[b] = min(next_dp[b],new_a)
            new_b = b + b_trace 
            if new_b < m:
                next_dp[new_b] =min(next_dp[new_b] , dp[b])
        dp = next_dp
    answer = min(dp)
    return -1 if answer == INF else answer 




##처음 접근하려했던 
# def solution(info,n,m):
#     answer = float("inf")
#     def DFS(i,a,b):
#         nonlocal answer 

#         if a>=n or b >=m:
#             return 
#         if a>=answer:
#             return 
#         if i ==len(info):
#             answer =a
#             return 
#         a_trace , b_trace = info[i]
#         DFS(i + 1, a + a_trace, b)
#         DFS(i + 1, a, b + b_trace)
#     DFS(0,0,0)
#     return -1 if answer == float("inf") else answer 



def soultion(info , n , m):
    INF = float("inf")
    dp = [INF] * m
    dp[0]=0
    for a_trace , b_trace in info:
        next_dp=[INF] *m
        for b in range(m):
            if dp[b] ==INF:
                continue
            new_a = dp[b] + a_trace 
            if new_a < n:
                next_dp[b] = min(next_dp[b],new_a)
            new_b = b+ b_trace
            if new_b <m:
                next_dp[new_b] = min(next_dp[new_b],dp[b])
        dp  = next_dp 

    return 



