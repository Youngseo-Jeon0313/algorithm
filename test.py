'''
웬만하면 '어떤 원소가 들어있는지'를 확인하려고 할 때 
dictionary를 쓰자 ! hash 형태로 저장하고 있기 때문에 조회시 O(1)이 걸림
dictionary = hash table
'''


import sys
input = sys.stdin.readline

# 22232
N, M = map(int,input().split())
files = []
for _ in range(N):
    files.append(input().rstrip())
extensions = {}
for _ in range(M):
    extensions[(input().rstrip())]=1

# 먼저 그룹으로 나눈다. -> 딕셔너리
dict = {}
for i in files:
    name, extension = i.split('.')
    if name in dict.keys():
        dict[name].append(extension)
    else:
        dict[name] = [extension]

List = list(dict.items())
List.sort()

for key, values in List:
    os_ok = []; os_no = []
    # os에서 인식하는 게 있는 것들
    for extension in values:
        if extension in extensions.keys():
            os_ok.append(extension)
        # 없는 것들
        else:
            os_no.append(extension)
    os_ok.sort(); os_no.sort()
    for extension in os_ok:
        print(key+'.'+ extension)
    for extension in os_no:
        print(key+'.'+extension)