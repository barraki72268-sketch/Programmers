def solution(n,q,ans):
    answer = 0
    queries = [set(row) for row in q]
    #q안에서 하나씩 꺼내서 그 숫자들중 중복된 애들은 제거
    code= []

    def dfs(start):
        nonlocal answer 
        if len(code) ==5:
            for query , expected in zip(queries,ans):
                count = sum(num in query for num in code)
                if count != expected:
                    return
            answer +=1 
            return 
        remaining = 5-len(code)
        
        for num in range(start,n-remaining+2):
            code.append(num)
            dfs(num+1)
            code.pop()
    dfs(1)
    return answer