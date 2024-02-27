```python

#[PG] 프로세스 - 큐!!

from collections import deque


def solution(priorities, location):
    answer = 1
    q = deque(priorities)
    index = location
    # location을 현재위치로 계속해서 두자.
    while len(q) > 1:
        num = q.popleft()
        MAX = max(q)
        if num < MAX:
            q.append(num)
            if index == 0:
                index = len(q) - 1
            else:
                index -= 1
        else:
            if index == 0:
                return answer
            else:
                answer += 1
                index -= 1

    return answer

```