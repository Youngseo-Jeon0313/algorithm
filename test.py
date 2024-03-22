# 구현 문제 그냥 브루트포스

from itertools import product

def solution(users, emoticons):
    data = list(product([10,20,30,40], repeat=len(emoticons)))

    answer = [0,0]
    for discountSort in data:
        emoticon_plus_num = 0
        emoticon_cost = 0
        for target_type, target_price in users:
            user_sum = 0
            for i, emoticon in enumerate(emoticons):
                if target_type <= discountSort[i]:
                    user_sum += int(emoticon // 100 * (100 - discountSort[i]))
            if user_sum>=target_price:
                emoticon_plus_num+=1
            else:
                emoticon_cost+=user_sum
        answer = max(answer, [emoticon_plus_num, emoticon_cost])    
            
    return answer