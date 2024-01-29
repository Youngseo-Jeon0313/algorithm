#택배상자
'''
5,4,3,2,1, | 10,9,8,7,6
1 -> 발견했다면 여기에서 멈추서 deq를 살핀다. 라는 stack 이용 방식 !
'''

def solution(order):
    target = 0
    num = 1
    stack = []
    while num < len(order)+1:
        stack.append(num)
        while stack and stack[-1]==order[target]:
            stack.pop()
            target +=1
        num+=1
    return target #order의 몇 개까지 성공했냐