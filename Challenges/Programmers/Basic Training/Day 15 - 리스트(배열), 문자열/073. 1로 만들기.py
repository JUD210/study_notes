# 문제 설명
# 정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다. 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.
# 10 / 2 = 5
# (5 - 1) / 2 = 4
# 4 / 2 = 2
# 2 / 2 = 1
# 위와 같이 4번의 나누기 연산으로 1이 되었습니다.
# 정수들이 담긴 리스트 num_list가 주어질 때, num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 3 ≤ num_list의 길이 ≤ 15
# 1 ≤ num_list의 원소 ≤ 30
#
# 입출력 예
# num_list           | result
# [12, 4, 15, 1, 14] | 11
#
# 입출력 예 설명
# 입출력 예 #1
# 12는 3번, 4는 2번, 15는 3번, 1은 0번, 14는 3번의 연산이 필요하기 때문에 총 11번의 연산이 필요합니다.


def solution(num_list):
    loop_cnt = 0
    for i in range(len(num_list)):
        while num_list[i] != 1:
            num_list[i] //= 2
            loop_cnt += 1

    return loop_cnt


# SOL 1
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)


# SOL 2
def solution(num_list):
    answer = 0
    for n in num_list:
        while n != 1:
            n //= 2
            answer += 1

    return answer
