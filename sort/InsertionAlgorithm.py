import random


# 두번째 인덱스 부터 시작
# 해당 인덱스 앞에 있는 데이터부터 비교하여 인덱스 값이 더 작으면 데이터를 뒤 인덱스로 복사

# 두번째 값부터 왼쪽값이랑 비교하는데 값이 작아지면 그 부분이랑 스왑... 계속 반복

def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data


data_list = random.sample(range(100), 10)
print(insertion_sort(data_list))
