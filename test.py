#1063
#y, x
movements = {'R':[0,1], 'L':[0,-1], 'B':[1,0], 'T':[-1,0], 'RT':[-1,1], 'LT':[-1,-1], 'RB':[1,1],'LB':[1,-1]}

board_x = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
#y좌표는 8-x 로 지정 !
K, S, N = input().split()
N=int(N)
K_pos = [8-int(K[1]), board_x[K[0]]] # y, x #int/str처리 주의
S_pos = [8-int(S[1]), board_x[S[0]]]
for _ in range(N):
    move = input()
    dy, dx = movements[move]
    # print(dy, dx)
    if 0<=K_pos[0]+dy<8 and 0<=K_pos[1]+dx<8:
        K_pos[0]+=dy
        K_pos[1]+=dx
        if S_pos == K_pos:
            if 0 <= K_pos[0] + dy < 8 and 0 <= K_pos[1] + dx < 8:
                S_pos[0] += dy
                S_pos[1] += dx
            else:
                K_pos[0] -= dy
                K_pos[1] -= dx
board_x_reverse = dict((v,k) for k,v in board_x.items())
K_ans = ''
K_ans+=board_x_reverse[K_pos[1]]
K_ans+=str(8-K_pos[0])

S_ans = ''
S_ans+=board_x_reverse[S_pos[1]]
S_ans+=str(8-S_pos[0])
print(K_ans)
print(S_ans)
