#10610
N=list(input())
N=sorted(N, reverse=True)
if N[-1]!='0':
    print(-1); exit()
sum = 0
for i in N: sum+=int(i)
if sum%3: print(-1); exit()
print(''.join(N))