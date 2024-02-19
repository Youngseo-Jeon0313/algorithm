def solution(beginning, target):
    answer = 0
    row = len(beginning[0]); col = len(beginning) #열, 행
    
    change_spot = [['0' for _ in range(row)] for _ in range(col)]
    
    for i in range(col):
        for j in range(row):
            if beginning[i][j]!=target[i][j]:
                change_spot[i][j]='1'
    standard = '0'
    for a in change_spot:
        if '1' in a:
            standard=''.join(a)
            break;
    for b in change_spot:
        compare = int(''.join(b),2)^int(standard,2)
        if compare == 0 or compare == 2**(len(change_spot[0]))-1:
            continue
        else: 
            return -1
    #일단 된다는 가정하에 최소 찾기
    answer_1 = 0; str_1='';
    answer_2 = 0; str_2='';
    for b in change_spot:
        compare = int(''.join(b),2)^int(standard,2)
        if compare == 0:
            answer_2 +=1
            str_1=b
        else:
            answer_1+=1
            str_2=b
    #print(answer_1, str_1, answer_2, str_2)
    for i in str_1: 
        if i=='1':
            answer_1+=1
    for j in str_2:
        if j=='1':
            answer_2+=1
            
    return min(answer_1, answer_2)
    