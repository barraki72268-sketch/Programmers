from collections import deque 

def solutions(storage,requests):
    n=len(storage)
    m = len(storage[0])
    board = [[""] *(m+2)]
    for row in storage:
        board.append([""] + list(row) + [""])
    board.append(([""] * (m+2)))
    directions = [(-1,0), (1,0),(0,-1),(0,1)]
    for r in requests:
        target = r[0]
        if len(r) ==2:
            for x in range(1,n+1):
                for y in range(1,m+1):
                    if board[x][y] == target:
                        board[x][y] ==""
        else:
            Q= deque([0,0])
            visited = [[False] * (m+2) for _ in range(n+2)]
            visited[0][0]= True
            remove = []
            while Q:
                x,y = Q.popleft()
                for dx, dy in directions:
                    nx = x+ dx
                    ny = y + dy
                    if not (0<=nx<n+2 and 0<= ny <m+2):
                        continue

                    if visited[nx][ny]:
                        continue
                    visited[nx][ny] = True
                    if board[nx][ny] == "":
                        Q.append((nx,ny))
                    elif board[nx][ny] == target:
                        remove.append((nx,ny))
        for x,y in remove:
            board[x][y] = ""
    answer = 0

    for row in board:
        for value in row:
            if value != "":
                answer += 1

    return answer

             

    