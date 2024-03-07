# 모두 다를 때 surprising

while True:
    flag=True
    s = input()
    if s=='*': break
    for i in range(1,len(s)): #step
        List = []
        for j in range(len(s)-i):
            List.append(s[j]+s[j+i])
        if len(List)!=len(set(List)):
            flag=False
    if flag:
        print(s+' is surprising.')
    else:
        print(s+' is NOT surprising.')