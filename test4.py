N = int(input())
T = input()
M = int(input())
prefix_sum = [[0 for _ in range(N+1)] for _ in range(ord('z')-ord('a')+1)]
for i in range(N-1, -1, -1):
    #해당 아스키코드
    ascii_code = ord(T[i])-ord('a')
    #print(ascii_code)
    for j in range(ord('z')-ord('a')+1):
        if j==ascii_code:
            prefix_sum[j][i]=prefix_sum[j][i+1]+1
        else:
            prefix_sum[j][i]=prefix_sum[j][i+1]
answer = 0

for _ in range(M):
    a,b=list(input())
    for i in range(N):
        if T[i]==a:
            print(prefix_sum[ord(b)-ord('a')][i])
            answer+=(prefix_sum[ord(b)-ord('a')][i])
print('답',answer)

        