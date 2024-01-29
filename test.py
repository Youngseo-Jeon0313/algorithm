#[PG] 숫자 카드 나누기


def gcd(a, b):  # 최대공약수
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


def solution(arrayA, arrayB):
    answer = 0
    gcd_A = arrayA[0]
    for i in range(len(arrayA)):
        gcd_A = gcd(gcd_A, arrayA[i])
    gcd_B = arrayB[0]
    for j in range(len(arrayB)):
        gcd_B = gcd(gcd_B, arrayB[j])

    print(gcd_A, gcd_B)

    flag = True
    for a in arrayA:
        if a % gcd_B == 0:
            flag = False
            break
    if flag: answer = max(answer, gcd_B)

    flag = True
    for b in arrayB:
        if b % gcd_A == 0:
            flag = False
            break
    if flag: answer = max(answer, gcd_A)
    return answer

'''
테스트케이스
6, 12, 18
4, 8, 16

답: 6  -> 처음부터 3이라고 생각해서 lcm을 같이 쓰게 됨
'''

#여기에서 array원소의 최댓값은 1억이었다. 따라서 lcm을 쓰는 아래 코드는 반드시 overflow(런타임 에러) 발생

'''
각 array의 최대공약수와 최소공배수를 구하자.
'''
def gcd(a,b): #최대공약수
    if a==0:
        return b
    else:
        return gcd(b%a, a)

def lcm(a,b): #최소공배수
    return int((a*b)/gcd(a,b))

def div(num):
    divlist = []
    for i in range(1,int(num**(1/2)) + 1):
        if num%i==0:
            divlist.append(i)
            divlist.append(num//i)
    return divlist

def solution(arrayA, arrayB):
    answer = 0
    lcm_A = arrayA[0]
    gcd_A = arrayA[0]
    for i in range(len(arrayA)):
        lcm_A = lcm(lcm_A, arrayA[i])
        gcd_A = gcd(gcd_A, arrayA[i])
    lcm_B = arrayB[0]
    gcd_B = arrayB[0]
    for j in range(len(arrayB)):
        lcm_B = lcm(lcm_B, arrayB[j])
        gcd_B = gcd(gcd_B, arrayB[j])
    divlist_A = div(gcd_A)
    divlist_B = div(gcd_B)
    #print(lcm_A, gcd_A, lcm_B, gcd_B)
    #print(divlist_A, divlist_B)
    for a in divlist_A:
        if lcm_B%a!=0:
            if a>answer: answer = a
    for b in divlist_B:
        if lcm_A%b!=0:
            if b>answer: answer = b
    return answer