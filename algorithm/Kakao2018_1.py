# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
#
# 비밀지도
# 네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.
#
# 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 공백(" ) 또는벽(#") 두 종류로 이루어져 있다.
# 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 지도 1과 지도 2라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
# 지도 1과 지도 2는 각각 정수 배열로 암호화되어 있다.
# 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

def solution(n, arr1, arr2):
    answer = []
    # n개 개수만큼 루프
    for index in range(n):
        # arr1과 arr2의 정수를 OR연산한 결과를 2진수로 변환한다. bin(arr1[index] | arr2[index])
        # 변환된 2진수의 값에는 0b의 값이 항상 존재하므로 제거한다. [2:]
        # 숫자가 작은 경우 2진수가 N개의 값으로 변환되질 않으므로 N개보다 작을 시 0을 붙인다. rjust(n, '0')
        # 배열로 변환한다. list()
        binary_or_list = list(bin(arr1[index] | arr2[index])[2:].rjust(n, '0'))
        # 변환된 배열을 1이면 #, 0이면 공백으로 변환 후 String으로 저장한다. ''.join, convert_value
        answer.insert(index, ''.join([convert_value(value) for value in binary_or_list]))
    return answer


def convert_value(value):
    if value == "0":
        return " "
    else:
        return "#"


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))