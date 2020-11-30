# https://programmers.co.kr/learn/courses/30/lessons/17676
from datetime import datetime

#
def solution(lines):
    answer = 0
    start_time, end_time = [], []
    for str_date in lines:
        str_date_arr = str_date.rsplit(" ", 1)
        start_time.append(get_diff_datetime(convert_epoch_time(str_date_arr[0]), str_date_arr[1].replace("s", "")))
        end_time.append(convert_epoch_time(str_date_arr[0]))
    max_count = 0
    for epoch_end in end_time:
        count = 0
        epoch_end_plus = epoch_end + 0.999
        for index in range(len(lines)):
            if not (end_time[index] < epoch_end or epoch_end_plus < start_time[index]):
                count += 1

        if count > max_count:
            answer = count

    return answer


def get_diff_datetime(epoch_time, diff_time):
    # 차이시간 계산
    diff_epoch_time = epoch_time - float(diff_time) + 0.001
    return diff_epoch_time


def convert_epoch_time(str_date):
    # 시간을 에포치 시간으로 변
    # "%Y-%m-%d %H:%M:%S.%f"
    return datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S.%f").timestamp()


lines = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"

    # "2016-09-15 20:59:57.421 0.351s",
    # "2016-09-15 20:59:58.233 1.181s",
    # "2016-09-15 20:59:58.299 0.8s",
    # "2016-09-15 20:59:58.688 1.041s",
    # "2016-09-15 20:59:59.591 1.412s",
    # "2016-09-15 21:00:00.464 1.466s",
    # "2016-09-15 21:00:00.741 1.581s",
    # "2016-09-15 21:00:00.748 2.31s",
    # "2016-09-15 21:00:00.966 0.381s",
    # "2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))
