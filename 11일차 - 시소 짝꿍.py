def solution(weights):
    answer = 0
    seen = {}
    for weight in sorted(weights):
        for a,b in ((1,1),(1,2),(2,3),(3,4)):
            if (weight * a)//b ==0:
                partner = weight *a //b
                answer += seen.get(partner,0)
        seen[weight] = seen.get(weight,0)+1
        
    return answer