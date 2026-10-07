def solution(plans):
    answer = []
    stack = []
    for name, start , duration in plans:
        si, bun = map(int,start.split(":"))
        stack.append((name, si*60 + bun, duration))
    sub = []
    for i,(name,start,duration) in enumerate(stack):
        sub.append((name,duration))
        if i == -1:
            break
        ava = stack[i+1][1] - start 
        while sub and ava > 0:
            current_name, remaining = sub[-1]
            if remaining <=ava:
                ava -= remaining
                answer.append(current_name)
                sub.pop()
            else:
                remaining -= ava
                ava = 0
        while sub:
            answer.append(sub.pop()[0])
    return answer






    return answer