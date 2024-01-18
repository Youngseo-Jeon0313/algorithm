# 바탕화면 정리

def solution(wallpaper):
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), -float('inf'), -float('inf')
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]=='#':
                print('here', i, j)
                min_x = min(min_x, j)
                min_y = min(min_y,i)
                max_x = max(max_x,j+1)
                max_y = max(max_y,i+1)
    #print(min_x, max_x, min_y, max_y)
    answer = [min_y, min_x, max_y, max_x]
    return answer