# def solution(sequence):
#     pulse1 = []
#     pulse2 =[]
#     for i, val in enumerate(sequence):
#         if i % 2 ==0:
#             pulse1.append(val)
#             pulse2.append(-val)
#         else:
#             pulse1.append(-val)
#             pulse2.append(val)
#     answer = float('-inf')
#     for pulse in (pulse1, pulse2):
#         curr_sum = 0
#         for val in pulse:
#             curr_sum = max(val , curr_sum+ val)
#             answer = (answer , curr_sum)
#     return answer
def solution(scores):
    wanho_a ,wanho_b = scores[0]
    wanho_sum  =  wanho_a + wanho_b
    scores.sort(key = lambda x:(-x[0],x[1]))
    max_b = -1 
    rank = 0
    for a,b in scores:
        if a > wanho_a and b> wanho_b:
            return -1 
        if b <max_b:
            continue
        max_b = max(b, max_b)
        if a+b > wanho_sum:
            rank +=1
    return rank