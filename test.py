# n+1 카드게임 카카오

def solution(coin, cards):
    # coin = 8; cards= [1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6, 7]
    answer = 1
    n = len(cards)
    visited = [0 for _ in range(n + 2)]
    mine = cards[:(n // 3)]
    picks = []
    turn = 2
    while n // 3 + turn <= n:
        flag = 0
        for i in mine:
            if not visited[i] and (n + 1 - i) in mine:
                visited[i] = 1;
                visited[(n + 1 - i)] = 1;
                answer += 1; flag = 1; turn += 2;
                print(1);
                break;
        if flag: continue
        for j in cards[(n // 3):(n // 3 + turn)]:
            if not visited[j] and (n + 1 - j) in mine and coin > 0:
                visited[j] = 1;
                visited[n + 1 - j] = 1;
                answer += 1; coin -= 1; flag = 2;
                turn += 2;
                print(2);
                break;
        if flag: continue
        for k in cards[(n // 3):(n // 3 + turn)]:
            if not visited[k] and (n + 1 - k) in cards[(n // 3):(n // 3 + turn)] and coin > 1:
                visited[k] = 1;
                visited[n + 1 - k] = 1;
                answer += 1; coin -= 2; flag = 3;
                turn += 2;
                print(3);
                break;
        if flag == 0:
            break;

    return answer

'''
그리디
어렵다…
범위 넘어가는 것 체크 필요 ! -> deq popleft 사용이 더 직관적이다.
집중해서 풀 필요가 있다..
테스트케이스 4까지 모두 파악해봤어야 함

'''