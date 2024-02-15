# 프로그래머스 - 표현 가능한 이진트리
'''
만들어지는 모든 이진수의 형태는 2^n-1이다. 그만큼 0을 앞에 채워야 함
그렇다면 안되는 경우는 ? -> 왼쪽 오른쪽 중에 갔는데, 안쪽이 '0'이라면 그 묶음의 합은 0이어야 한다.
0초과면 안됨으로 처리
'''
import math


def solution(numbers):
    answer = []

    def dfs(num):
        # print(num)
        if len(num) == 1:  # 된다.
            return 0

        num_len = len(num) // 2
        left = num[:num_len]
        mid = num[num_len]
        right = num[(num_len + 1):]

        if mid == '1':  # 된다.
            return dfs(left) + dfs(right)
        else:  # 밑에가 다 0이여야 함
            if '1' in left + right:
                return 1
            else:
                return 0

    for i in numbers:
        num = (bin(i))[2:]
        LEN = len(num)
        N = math.ceil(math.log2(LEN + 1))
        num = num.zfill(2 ** (N) - 1)
        # print(num)
        ans = dfs(num)
        if ans == 0:
            answer.append(1)  # 싹 다 0이 나와야지만 가능 !
        else:
            answer.append(0)

        # print("=====================")
    return answer