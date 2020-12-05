# https://programmers.co.kr/learn/courses/30/lessons/17687
"""
    N진수 게임
    [해결방법]
        - N 진법으로 변환하는 함수를 하나 작성한다.
        - 0부터 시작해서 t의 값이 될때까지 무한루프를 한다.
        - 만들어진 진법으로 변환된 값을 다시 루프한다.
        - 스위치 변수에 m의 값이 될때마다 초기화가 되도록 만들어 p의 순서가 될때마다 결과에 저장한다.
        - 변수에 넣을 때는 Pop을 사용
        - 진법 변환의 결과 데이터중, 10이상의수는 A,B,C,D,E로 나타내므로 최대값이 16진수의 정수형으로 변환한다.

    [입출력 예제]
    n	t	m	p	result
    -------------------------------------
    2	4	2	1	0111
    16	16	2	1	02468ACE11111111
    16	16	2	2	13579BDF01234567
"""


def solution(n, t, m, p):
    answer = ''
    number_index = 0
    # 정답 숫자 개수
    t_index = 0
    # 스위치 변수
    p_index = 1
    while True:
        # 16진수로 변환
        value_list = [hex(value)[2:].upper() for value in convert(number_index, n)]
        # print('값 >> {}'.format(value_list))
        while value_list:
            temp_val = value_list.pop()
            # print('{} % {} = {}'.format(number_index, m, number_index % m))
            # print(temp_val)
            if p_index == p:
                answer += str(temp_val)
                # print('p값을 저장해야하는곳 {}'.format(value_list))
                t_index += 1
                #조건 추가
                if t_index == t:
                    break
            # else:
                # print('버려지는 애들 {}'.format(value_list))

            # print('=------')
            # 초기화
            if p_index == m:
                p_index = 1
            else:
                p_index += 1
        number_index += 1
        if t_index == t:
            break

    return answer


def convert(num, n):
    num_list = []
    while True:
        # 첫번째 값이 0 일 경우 처리
        if num < n:
            num_list.append(num)
            return num_list
        quotient, remainder = divmod(num, n)[0], divmod(num, n)[1]
        num_list.append(remainder)

        if quotient < n:
            # 마지막 값은 몫도 추가해야
            num_list.append(quotient)
            break
        # 기본값을 몫의 값으로 변환
        num = quotient

    # num_list.reverse()
    return num_list


print(solution(16, 16, 2, 1))
