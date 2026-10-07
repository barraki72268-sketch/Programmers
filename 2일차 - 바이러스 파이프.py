from collections import deque

def solution(n,infection ,edges , k):
    graph =[[] for _ in range(n+1)]

    for x,y,pipe_type in edges:
        graph[x].append((y,pipe_type))
        graph[y].append((x,pipe_type))
    answer = 1

    #BFS로 감염상태 복사 
    def spread(infected , pipe_type):
        new_infected = infected.coy()
        Q = deque(infected)
        while Q:
            curr= Q.popleft()
            for nxt, edge_type in graph[curr]:
                if edge_type != pipe_type:
                    continue
                if nxt in new_infected:
                    continue
                new_infected.add(nxt)
                Q.append(nxt)
        return new_infected
    def DFS(count, infected, last_type):
        nonlocal answer 
        answer = max(answer ,len(infected))

        if count ==k or answer ==n:
            return 
        for pipe_type in (1,2,3):
            if pipe_type == last_type:
                continue
            new_infected = spread(infected, pipe_type)

            if new_infected == infected:
                continue
            DFS(count +1 , new_infected,pipe_type)
    DFS(0,{infection},0)
    return answer
