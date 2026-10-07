# def solution(points, routes):
#     def DFS(x,y,end_x, end_y, path):
#         path.append((x,y))

#         if x ==end_x and y==end_y:
#             return 
#         if x < end_x:
#             DFS(x+1, y, end_x,end_y,path)
#         elif x> end_x:
#             DFS(x-1, y, end_x, end_y, path)
#         elif y< end_y:
#             DFS(x,y+1, end_x ,end_y ,path)
#         elif y > end_y:
#             DFS(x,y-1, end_x ,end_y ,path)
#     all_path = []
#     for route in routes:
#         robot_path = []
#         for i in range(len(route) -1):
#             start_x , start_y = points[route[i]-1]
#             end_x , end_y = points[route[i+1] -1 ]
#             segment = []
#             DFS(start_x,start_y,end_x,end_y , segment)
#             #extend 문법 알기 
#             # append를 하면 구간 끝인데 우린 노드 이동 모두 하나의 경로로 묶어야 하니 
#             if i==0:
#                 robot_path.extend(segment)
#             else:
#                 #출발 -> 끝 ->출발 여기 겹치니깐 
#                 robot_path.extend(segment[1:])
#         all_path.append(robot_path)
#     answer = 0
#     max_time= max(len(path) for path in all_path)
#     for t in range(max_time):
#         #딕셔너리 기억 
#         positions = {} # 그 시각에 각 좌표에 로봇이 몇 대 있는지 
#         for path in all_path:
#             if t<len(path):
#                 pos = path[t]
#                 #이거 반드시 기억
#                 positions[pos] = positions.get(pos,0) +1 
#         for count in positions.values():
#             if count >=2:
#                 answer +=1
#     return answer 
