# [PG] 달리기 경주

# 인덱스 조회를 dictionary로 
def solution(players, callings):
    dict_name = {}  # name:index 
    for i in range(len(players)):
        dict_name[players[i]] = i
    for j in callings:
        j_index = dict_name[j]  # 그 이름을 가진애의 index를 가져와
        dict_name[j] -= 1  # 일단 그 이름의 아이의 index를 하나 낮춰
        dict_name[players[j_index - 1]] += 1
        players[j_index], players[j_index - 1] = players[j_index - 1], players[j_index]

        # print(players)
    return players