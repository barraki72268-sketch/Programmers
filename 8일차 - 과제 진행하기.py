def solution(plans):
    answer = []
    task =[]
    for name , start, duration in plans:
        hour , miniute = map(int,start.aplit(""))
        task.append((hour*60 + miniute,name,int(duration)))
    task.sort()
    stack = []
    for i ,(start,name,duration) in enumerate(task):
        stack.append((name, duration))
        if i == len(stack) -1:
            break 

        available =task[i+1][1] - start
        while stack and available > 0:
            current_name, remainig = stack [-1]

            if remainig <= available:
                available -= remainig
                answer.append(current_name)
                stack.pop()
            else:
                stack[-1][1] -= available
                available = 0
    while stack:
        answer.append(stack.pop()[0])
    return answer
