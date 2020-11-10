import random


# 버블정렬
# 두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘
#   데이터의 길이 -1번만큼 비교루프
# 데이터 스왑이 한번도 일어나지 않으면 프로세스를 더이상 수행하지 않는다. ( 정렬이 이미 되어있다 )
# 알고리즘 복잡도는 for loop가 2번이기 때문에 O(n의 제곱), 최선은 O(n) - 정렬이 이미 되어있을때
def bubble_sort(data):
    for first_index in range(len(data) - 1):
        swap = False
        for second_index in range(len(data) - first_index - 1):
            if data[second_index] > data[second_index + 1]:
                # Swap 하는 방법
                data[second_index], data[second_index + 1] = data[second_index + 1], data[second_index]
                swap = True

        # !swap, swap == False
        if not swap:
            break
    return data


data_list = random.sample(range(100), 50)
print(bubble_sort(data_list))
