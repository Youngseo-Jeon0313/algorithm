# PG 롤케이크 자르기

def solution(topping):
    #앞에서부터 / 뒤에서부터 파악
    answer = 0
    dict = {}
    prefix_sum = [0 for _ in range(len(topping)+1)]
    for i in range(len(topping)):
        if topping[i] in dict.keys():
            prefix_sum[i+1]=prefix_sum[i]
        else:
            dict[topping[i]]=1
            prefix_sum[i+1]=prefix_sum[i]+1
    #print(prefix_sum)
    prefix_sum2 = [0 for _ in range(len(topping)+1)]
    topping_new = topping[::-1]
    dict2 = {}
    for j in range(len(topping_new)):
        if topping_new[j] in dict2.keys():
            prefix_sum2[j+1]=prefix_sum2[j]
        else:
            dict2[topping_new[j]]=1
            prefix_sum2[j+1]=prefix_sum2[j]+1
    #print(prefix_sum2)
    for k in range(len(topping)-1):
        if prefix_sum[k]==prefix_sum2[len(topping)-k]:
            answer+=1
    return answer
