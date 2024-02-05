# [PJ] 땅따먹기

def solution(land):
    #land = [[1,2,3,4]]
    answer = 0
    DP = [[0 for _ in range(4)] for _ in range(len(land))]
    # DP init
    for i in range(4):
        DP[0][i]=land[0][i]
    for j in range(1, len(land)):
        for k in range(4):
            DP[j][k]=land[j][k]
            DP[j][k]+=max(DP[j-1][(k+1)%4], DP[j-1][(k+2)%4], DP[j-1][(k+3)%4])
    answer = (max(DP[len(land)-1]))
    return answer