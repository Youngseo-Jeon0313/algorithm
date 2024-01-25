## 프로그래머스 할인행사
def check(number, now):
    for i in range(len(number)):
        if number[i]!=now[i]:
            return False
    return True

#슬라이딩 윈도우 같은 투포인터
def solution(want, number, discount):
    answer=0
    N = len(discount)
    dict = {}
    for i in range(len(want)):
        dict[want[i]]=i
    now = [0 for _ in range(len(want))]
    #init
    for j in range(10):
        if discount[j] in dict.keys():
            now[dict[discount[j]]]+=1
    left=0; right = 10
    while True:
        if check(number, now):
            answer+=1
        if right==N: break
        if discount[left] in dict.keys():
            now[dict[discount[left]]]-=1;
        if discount[right] in dict.keys():
            now[dict[discount[right]]]+=1;
        left+=1; right+=1;
    return answer