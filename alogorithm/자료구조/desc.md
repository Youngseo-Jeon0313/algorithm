stack, deque ..


## 스택
- 스택에 넣을 수 있는 자료의 종류는 다양하다.   
어떤 상태의 최종값을 넣을 수도 있지만   
[0,0,0,0,0,0,0]    
[0,0,0,0,0,0,7]    
이런식으로 과정 상의 값들이 계속되어 popleft() append() 될 수 있다.   
ex) PG 다리를 지나는 트럭   

- 과정을 그려볼 때   
<------- 이런 어떤 "선" 상의 상자 움직임 현상이 일어난다면 stack이나 deq를 의심하자!

- [[][[]]] -> 이런 종류의 문제 stack 유리

- 오큰수 : while문과 stack 활용
```python
n = int(input())
arr = list(map(int, input().split()))
answer = [-1 for _ in range(n)]
stack = []

for i in range(n):
  while stack and arr[stack[-1]] < arr[i]: 
    answer[stack.pop()] = arr[i]
  stack.append(i)

for i in range(n):
  print(answer[i], end=' ')
```
```
다음과 같이 하나씩 돌면서 numbers[i]가 '가까운 가장 큰 수'인  것들을 stack에서 뽑으면서 값을 할당하는 것이다.
그리고 stack에는 다시 index 값 i를 넣는다. -> 얘도 판단의 미로 속으로 들여보내는 것.! 나중에 stack에서 뽑히면 가장 가까운 큰 수가 할당될 예정이다.

뒤에 큰 수가 더이상 없는 경우들이 있을 때는 -1로 출력해주기로 했으므로 answer는 -1로 초기화시킨다.
```
## deq
- 시뮬레이션에서 deq에서 popleft()와 pop() 방향 주의

- deque은 시뮬레이션에서, 이럴 때 강하다! 상하 좌우로 움직이며 조건에 만족하는 것을 포함시키고자 할 때    
만약 2차원 배열 안에서    
특정 퍼즐모양을 여러 개 찾고자 한다면 이중 덱도 사용 가능하다.

## dict
-> from collections import defaultdict
하면 defaultdict(int) 시 0으로 자동 생성되기 때문에 +=1 등의 처리를 해줘도 된다.
dict는 key가 문장일 때 강력하다.
아래와 같이 리스트와 딕셔너리를 같이 사용 가능 !
menus = [{} for _ in range(11)]

- dict가 주는 장점 !! -> O(1) 의 시간복잡도를 가진다는 것이다.
ex. [PG]달리기 경주 
.index() 로 가져올 때 O(N)이 걸리는 문제를 최적화하기 위해 dictionary를 쓸 수 있다. 

### queue
- ex. [PG] 프로세스 - 큐!!
deq을 이용해 프로세스 중 어떤 한 원소가 언제 처리되는지에 대해 알아보는 문제 ! 매우 좋음...   
해당 위치 자체를 global 원소로 데려가 위치를 계속해서 판단해준다.    
시간복잡도 고민 잘하자.    
처음에는 100! 일 거라고 생각했다. 하지만 우선순위 숫자가 9이기 때문에 최악의 경우 10! = 3628800 정도라 괜찮다.

### while 문 & deque
굳이 규칙 / 예외케이스 로 해결하려하지 말고 while문 두 개 & deque으로 해결 !   

스택/큐로 해결할 수 있는 건 해결하자 !   