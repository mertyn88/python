# https://programmers.co.kr/learn/courses/30/lessons/17678
# from datetime import datetime
import datetime

"""
    [해결방법]
        - 시간계산을 epoch_time으로 변경하여 계산한다.
            - 시간에 대해 연산을 할때에는 :나 공백같은 문자열이 포함되어있으며 시간이나 분단위가 넘어갈수 있으므로 시간을 숫자로 표현하는 epoch시간으로 변경하여 연산한다.
            - 단 해당 문제에서는 시간과 분만 있으면 되므로 %H와 %M만 이용한다.
            - 파이썬에서 1970년도(%Y)를 추가적으로 입력하지 않으면 1900년도로 인식을하고 그로 인해 1970년도 부터 계산되는 epoch시간이 음수값으로 나오게된다. 해서 1970을 고정한다.
            - 정답시에는 %H:%M의 형태가 되어야 하므로 epoch_time에서 datetime으로 변경하는 로직을 추가한다.
        - while true로 n(반복횟수)의 값이 0이 될때까지 반복한다.
        - t(운행간격) * 60을 하여 분단위를 초단위로 변경하고 루프당 추가되어야 할 시간을 계산한다.
        - 버스 출발시간은 09:00으로 고정이다. ( epocho_time = 32400 )
        - 루프당 m(남은자리)를 없에는 방식으로 하며 버스 출발시간이 더 클때에 리스트를 pop하여 자리를 없엔다.
        - 단, pop할 시에 마지막에 자리가 없을때 가장 늦은 자리시간에 -1분을 해야하므로 diff_time변수에 담아서 처리한다.
        - 24:00 일경우 , 00:00으로 변경한다. ( 시간범위가 24시간단위인데 24:00인경우는 잘못된 경우다. 문제가 잘못된거같다. 00:00으로 치환해야 에러가 발생하지 않는다.) 
"""


def solution(n, t, m, timetable):
    # Validation Check
    # 문제에서 다른값을 줄일은 없겠지만 하는김에 validation 체
    if not validation(n, t, m, timetable):
        return "00:00"

    # timetable 정렬
    # timetable.sort()
    # 주어진 배열의 시간이 오름차순, 또는 내림차순으로 되어있지 않고, pop기능을 사용하기 위해 내림차순으로 정렬
    timetable.sort(reverse=True)
    # print('정렬된 값 {}'.format(timetable))

    # timetable을 에포치 시간으로 변경
    time_list = [str_to_epoch(value) for value in timetable]

    # t의 값을 초로 변환
    loop_second = t * 60
    # 버스 최초 출발 시간 09:00
    current_time = 32400
    # Loop 범위는 00:00 ~ 23:59 / 0  ~ 86340
    while True:
        # print('반복 횟수 {}, 시간 {}'.format(n, current_time))
        # 남아있는 배열의 마지막값(제일 작은값)을 비교타임으로 선정, -1값은 배열의 가장 마지막 값을 지칭함, pop을 사용하면 실제로 제거되므로 이때 사용하면 안된다.
        diff_time = time_list[-1]

        # 남은 버스 자리
        empty_num = m
        for index in range(0, m):
            # 배열의 개수가 0이상이며, 버스출발 시간보다 작은 데이터는 pop한다.
            if len(time_list) > 0 and current_time >= time_list[len(time_list) - 1]:
                diff_time = time_list.pop()
                empty_num -= 1

        # 남은 자리
        #print('남은자리 {}'.format(empty_num))
        # 횟수 차감
        n -= 1
        # n의 값이 0일 경우, 실제 결과를 얻기위한 작업이 필요하다.
        if n == 0:
            if empty_num > 0:
                # 남은 자리가 0이상인 경우, 느긋하게 가도 되니까 해당 출발시간이 곧 정답
                answer = epoch_to_date(current_time)
            else:
                # 남은 자리가 없으므로 마지막 버스를 타려면 자리가 없는 시간의 -1분을 해야함
                answer = epoch_to_date(diff_time - 60)
            break

        # 다음 루프를 위한 시간 증가
        current_time += loop_second
    return answer


def validation(n, t, m, timetable):
    if not 0 < n <= 10:
        print('n값이 범위를 벗어났습니다.')
        return False
    if not 0 < t <= 60:
        print('t값이 범위를 벗어났습니다.')
        return False
    if not 0 < m <= 45:
        print('m값이 범위를 벗어났습니다.')
        return False
    if not 1 <= len(timetable) <= 2000:
        print('시간 범위가 잘못되었습니다.')
        return False
    return True


# 버스 출발시간 32400.0


def str_to_epoch(str_date):
    if str_date == '24:00':
        str_date = '00:00'

    # 시간을 에포치 시간으로 변환, 단 1970년도로 시작하게 끔 하며 초단위까지, KST시간을 위해 + 9시
    # "%Y-%m-%d %H:%M:%S.%f"
    return int(datetime.datetime.strptime('1970 ' + str_date, "%Y %H:%M").timestamp()) + 32400


def epoch_to_date(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time - 32400).strftime('%H:%M')


# timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
timetable = ["09:10", "09:09", "08:00"]

print(solution(2, 10, 2, timetable))

# print(str_to_epoch("00:00"))
print(str_to_epoch("24:00"))
