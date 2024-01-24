# 17609
'''
1. 회문이라는 가정
- 짝수
- 홀수
2. 유사회문이라는 가정
- 짝수
    - 왼쪽 꺼에서 한 개를 제외한다.
    - 오른쪽 꺼에서 한 개를 제외한다.
- 홀수
    - 왼쪽 꺼에서 한 개를 제외한다.
    - 오른쪽 꺼에서 한 개를 제외한다.
'''


T = int(input())

for _ in range(T):
    answer = 0
    s = input()

    left = 0; right = len(s)-1
    while left<right:
        if s[left]==s[right]:
            left+=1; right-=1
        else:
            answer=1
            break
    if answer ==0: print(0); continue
    #유사회문이라고 가정
    #왼쪽 꺼에서 한 개를 제외하겠다.
    left = 0;
    right = len(s) - 1
    flag=0
    while left < right:
        #print(left, right, s[left], s[right])
        if s[left] == s[right]:
            left += 1; right -= 1
        else:
            if flag==0: left+=1; flag=1;
            else: flag=2; break
    if flag == 1:
        answer = 1;
        print(answer)
        continue
    #오른쪽 꺼에서 한 개를 제외하겠다.
    left = 0;
    right = len(s) - 1
    flag = 0
    while left < right:
        #print(s[left], s[right])
        if s[left] == s[right]:
            left += 1;
            right -= 1
        else:
            if flag == 0: right -= 1; flag = 1;
            else:
                flag = 2; break
    if flag == 1: answer = 1;
    else: answer = 2

    print(answer)