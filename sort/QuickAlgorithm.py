import random


# 퀵정렬
# 기준점(피봇)을 정해서, 기준점보다 작은 데이터는 왼쪽, 큰 데이터는 오른쪽으로 모으는 함수를 작성
# 각 왼쪽, 오른쪽은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복
# 함수는 왼쪽 + 피봇 + 오른쪽을 리턴
# 정렬 알고리즘 꽃...? 파이썬이랑 잘 어울리는 코드라고함

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    # 일반적인 공통 언어적 방
    # left, right = list(), list()
    # for index in range(1, len(data)):
    #    if pivot > data[index]:
    #        left.append(data[index])
    #    else:
    #        right.append(data[index])

    # 해당 방식이 더 간결하지만 전체 루프를 두번돌아서 시간은 더 걸린다.
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot < item]

    return quick_sort(left) + [pivot] + quick_sort(right)


data_list = random.sample(range(100), 10)
print("정렬전 값 {}".format(data_list))
print(quick_sort(data_list))
