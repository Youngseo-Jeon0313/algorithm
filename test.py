# [PG] 요격 시스템

'''
어차피 다 적용해줘야 해서 그리디임
우선 정렬하자 !
'''

def solution(targets):
    targets = sorted(targets, key=lambda x:x[1])
    #맨 뒤에서부터 한 개씩 가장 메인이 되는 애들 가져옴
    main_left, main_right = targets[0] #10, 14
    answer = 1
    for i in range(len(targets)):
        #그 사이에 겹치는 게 있는지 체크
        left, right = targets[i]
        #print(main_left, main_right, left, right)
        if main_right<=left: #바깥으로 나간 경우
            main_left, main_right = left, right
            answer+=1
    return answer

