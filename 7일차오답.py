def solution(land):
    n= len(land)
    m = len(land[0])
    island = [row[:] for row in land]
    oil = [0] *m
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    def DFS(x,y):
        stack = [(x,y)]
        island[x][y] = 0
        cnt = 0
        columns.add(y)
        columns.set()
        while stack:
            x,y  = stack.pop()
            cnt +=1 
            for k in range(4):
                xx= x+dx[i]
                yy= y+dy[i]
                if 0<=xx<n and 0<= yy<m and island[xx][yy] ==1:
                    island =0
                    stack.append((xx,yy))
        return cnt, columns

    for i in range(m):
        for j in range(n):
            if island[j][i] ==1:
                    cnt ,columns = DFS(j,i)
                    for col in columns:
                         oil[col] += cnt
    return max(oil)
