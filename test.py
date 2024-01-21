# 시소 짝꿍

def solution(weights):
    #weights = [100,100,100,100,100,100,200, 200, 200]
    List = [0 for _ in range(10001)]
    for weight in weights:
        List[weight]+=1
    answer = 0
    weights=sorted(weights)
    for i in weights:
        if i*1<10001 :
            if List[i]>1:
                #print(i,i)
                answer+=(List[i]*(List[i]-1))//2
        if i*3%2==0 and i*3//2 < 10001:
            if List[i*3//2]:
                #print(i,i*3//2)
                answer+=List[i]*List[i*3//2]
        if i*2 and i*2<10001:
            if List[i*2]:
                #print(i,i*2)
                answer+=List[i]*List[i*2]
        if i*4%3==0 and i*4//3 < 10001:
            if List[i*4//3]:
                #print(i,i*4//3)
                answer+=List[i]*List[i*4//3]
        List[i]=0
    return answer

# nC2 갯수 -> 그냥 계산 가능 (n*(n-1))//2
'''testcase
100,100,100,100,100,100->15
100,100,100,100,100,100,200 ->21
100,100,100,100,100,100,200,200,200 -> 36

'''