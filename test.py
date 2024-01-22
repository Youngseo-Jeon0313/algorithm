### 마법의 엘리베이터
def solution(storey):
    answer = 0
    div = 10
    while storey > 0:
        # print(storey)
        if storey % div > 5:
            # 더해
            answer += 10 - (storey % div)
            storey += 10 - (storey % div)
        elif storey % div == 5: #나머지가 5다.
            if storey > div and (storey // 10) % 10 > 4: #
                answer += 10 - (storey % div)
                storey += 10 - (storey % div)
            else:
                answer += storey % div
                storey -= (storey % div)
        else:
            answer += storey % div
            storey -= (storey % div)

        storey //= div

    return answer

"""
testcase
5 -> 5
6 -> 5
2564 -> 15
45 -> 9
55 -> 10
65 -> 9
555 -> 14 *****

"""