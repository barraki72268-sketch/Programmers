#선인장 (슬라이딩 윈도우 문제 암기)
from collections import deque
# def sliding_min(arr,size):
#     dq =deque()
#     result = []
#     for i ,val in enumerate(arr):
#         while dq and dq[0] <= i-size: #이걸 왜 하냐? 항상 윈도우를 벗어나지 않게 2x2라면 2를 벗어나면 안되니깐 
#             dq.popleft()
#         while dq and arr[dq[-1]] >= val: #덱에 저장 되어 있는값은 계속 최소값으로 해야 하니 
#             dq.pop()
#         dq.append(i)
#         if i >=size-1:#총 4개가 저장 되게끔 
#             result.append(arr[dq[0]])
#     return result
#슬라이딩 
def sliding_min(arr,size):
    dq =deque()
    re = []
    for i,val in enumerate(arr):
        while dq and dq[0] <=i-size:
            dq.popleft()
        while dq and arr[dq[-1]] >= val:
            dq.pop()
        dq.append(i)
        if i >= size -1:
            re.append(arr[dq[0]])
            #size 2 고 무한대 4  3 라면 dq.append(0) if 0 >= 2-1 Fasle dq[0]
            # 2번쨰 걸리면서 무한대 팝, dq[1] arr[4]
            # 1 <= 0x 2ㅂㄴ째 4>= 3 dq[2] arr[4,3]

def sliding_min(arr, size):
    dq = deque()
    re =[]
    for i , val in enumerate(arr):
        while dq and dq[0] <= i-size:
            dq.popleft()
        while dq and arr[dq[-1]] >= val:
            dq.pop()
        dq.append(i)
        if i >= size -1:
            re.append(arr[dq[0]])

def solution(m,n,h,w,drops):
    INF = len(drops) +1 
    rain = [[INF] * n for _ in range(m)]

    for t,(r,c) in enumerate(drops,start = 1):
        rain[r][c] = t
    row_min = []
    for row in rain:
        result = sliding_min(row,w)
        row_min.append(result)
    best_time = -1
    answer =[m,n]
    for c in range(n-w+1):
        col = [row_min[r][c] for r in range(m)]
        area_min = sliding_min(col,h)
        for r,first_r in enumerate(area_min):
            if first_r > best_time:
                best_time = first_r
                answer=[r,c]