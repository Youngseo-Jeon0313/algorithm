import sys
input = sys.stdin.readline

answer = float('inf')
answer_List = []
def back(node,a,b,c,d,cost):
    global answer; global answer_List;
    if cost>answer: return
    if a>=cond[0] and b>=cond[1] and c>=cond[2] and d>=cond[3]:
        if answer>cost:
            answer = cost
            answer_List = visited.copy()
        return
    for j in range(node,N-1):
        print(j+1)
        target = j+1
        visited.append(target)
        temp_a, temp_b, temp_c, temp_d, temp_e = List[target]
        back(target,a+temp_a,b+temp_b,c+temp_c,d+temp_d,cost+temp_e)
        visited.pop()
N=int(input()) # N이 작아서 브루트포스
visited = []
cond = list(map(int,input().split()))
List = []
for i in range(N):
    List.append(list(map(int,input().split())))

back(-1,0,0,0,0, 0)
if answer==float('inf'):
    print(-1); exit()
print(answer)
for index in range(N):
    if answer_List[index]:
        print(index+1, end =' ')
print()