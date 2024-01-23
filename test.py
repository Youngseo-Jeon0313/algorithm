### 혼자 놀기의 달인

from collections import defaultdict


def solution(cards):
    # cards = [2,4,5,1,3]
    parent = [i for i in range(len(cards))]

    def find(a):
        if a == parent[a]: #여기 생각하기 !!
            return a
        parent[a] = find(parent[a])
        return parent[a]

    def union(a, b):
        a = find(a)
        b = find(b)
        if b < a:
            parent[a] = b
        else:
            parent[b] = a

    answer = 0
    for i in range(len(cards)):
        union(i, cards[i] - 1)

    for i in range(len(cards)):
        find(i)
    dict = defaultdict(int)
    for j in parent:
        dict[j] += 1

    List = list(dict.items())
    List = sorted(List, key=lambda x: -x[1])
    # 딕셔너리에서 가장 큰 거 두 개 가져오기
    if len(List) == 1:
        return 0
    else:
        answer = (List[0][1] * List[1][1])
    return answer