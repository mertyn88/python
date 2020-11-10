import random


# 선택정렬
# 주어진 데이터 중, 최소값을 찾음
# 해당 최소값을 데이터 맨 앞에 위치한 값과 교체
# 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복
# 비교인덱스     |       비교시작        |       비교끝
#   0         |         1           |       Data - 1
#   1         |         2           |       Data - 1
#   2         |         3           |       Data - 1

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        # for loop가 전부 수행되고 나서 가장 작은값 lowest를 stand와 치환
        data[lowest], data[stand] = data[stand], data[lowest]
    return data


data_list = random.sample(range(100), 10)
print(selection_sort(data_list))
