def solution(users, emoticons):
    answer = [0,0]
    stack = []
    def dfs():
        if len(stack) == len(emoticons):
            subscriber = 0
            revenue = 0
            for min_discount , limit in users:
                total = 0
                for i in range(len(emoticons)):
                    discount = stack[i]
                    if discount >= min_discount:
                        total += emoticons[i]*(100-discount)//100
                if total >= limit:
                    subscriber +=1 
                else:
                    revenue += total
            if [subscriber,revenue] > answer:
                answer[:] = [subscriber,revenue]
            return 
        for discount in [10,20,30,40]:
            stack.append(discount)
            dfs()
            stack.pop()

    dfs()
    
    return answer