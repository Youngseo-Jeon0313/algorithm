#2011
'''
경우
- 건너뛴다.
- 수를 넣는다.
    - 앞 숫자랑 합친다. = 합칠 수 있는지 봐야 하고, 앞앞 상황 반영
    - 안 합친다. = 앞 상황 반영
22114
'''
dict = {str(i+1):chr(ord('A')+i) for i in range(26)}
N=(input())
N=' '+N
LEN = len(N)

List = [0 for _ in range(LEN+1)] #건너뛴다/수를 넣는다.

for i in range(LEN):
    temp = 0
    if i>0 and N[i-1:i+1] in dict.keys():
        temp+=max(1,1*List[i-2])
    if N[i] in dict.keys():  # 2다.
        temp += max(1,1*List[i-1])
    List[i]=temp
    if i>0 and temp==0: print(0); exit()


print(List[LEN-1]%1000000)