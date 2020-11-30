# https://programmers.co.kr/learn/courses/30/lessons/17684
# 재귀루프 횟수 변경을 위한 import
import sys

"""
    압축
    [해결방법]
        - 해당 문제의 첫번째는 A ~ Z 까지의 딕셔너리 형태의 변수에 A ~ Z 까지의 값을 설정하는것이다. (사전구축)
        - 일일이 넣는것보다는 아스키 코드값으로 루프를 하여 초기 사전을 구축한다.
        - global 이라는 전역변수를 많이 사용했다.
        - 재귀함수를 이용하여 값이 있으면 기존 값 + N 하여 점점 사전의 값을 추가한다.
        - switch 변수를 하나 만들어서 (temp_check) 해당 변수의 값이 있는 경우 pop한다. ( if에서 true가 발생하였다가 다시 true가 발생하면 이전의 값을 지워야한다. 예) K 다음에 KA도 사전에 있으면 기존의 K는 삭제되어야한다.)
        - list의 pop을 이용하여 처리함 ( 그로인하여 list를 reverse )
        - 파이썬은 재귀함수를 1000번까지만 기본적으로 허용하는데 예제에 1000글자가 넘거나 딱 1000글자여서 내 로직의 루프가 1000번 이상이되어서 에러남. import sys를 하여 재귀 루프를 2000번으로 변경
"""

# 사전 변수
global index_dic
index_dic = {}

# 결과 list
global result_list
result_list = []

# 사전 키
global index
index = 1

# 임시 리스트, if값이 none이 발생하였을때 temp_list에서 pop하여 등록
global temp_list값
temp_list = []

# 스위치 변
global temp_check
temp_check = 0


def solution(msg):
    # 재귀함수 2000번으로 증가 기본값 1천번수
    sys.setrecursionlimit(2000)

    # 사전 만들기 초기화 아스키 코드 65 ~ 90번까지
    global index
    for i in range(65, 91):
        index_dic[chr(i)] = index
        index += 1

    # print(index_dic)

    # 알파벳 리스트 역순으로 정렬
    char_list = list(msg)
    char_list.reverse()

    # 시작할때 처음 마지막 1글자로 시작
    get_char(char_list, char_list.pop())

    # 만들어진 결과 알파벳 사전에서 키값(숫자)로 변경 후 return
    answer = [index_dic.get(value) for value in result_list]
    return answer


# 재귀함수 주요 로직
def get_char(char_list, str):
    global index
    global temp_check

    # 사전에 전달받은 파라미터 str이 있는 경우 ( Java contains )
    if str in index_dic:
        # 전의 값에 사전이 있어서 다시 호출되었는데 또 사전에 있는 경우 기존값을 삭제한다.
        if temp_check > 0:
            result_list.pop()

        # 결과값에 추가
        result_list.append(str)

        # char_list가 0이 아니면 수행, char_list를 지속적으로 pop하므로 점점 개수가 줄어든다.
        if not len(char_list) == 0:
            # switch 변수 증가
            temp_check += 1
            # 임시 변수에 pop
            temp_val = char_list.pop()
            # 임시 list 변수에 저장
            temp_list.append(temp_val)
            # 기존값 + 신규값(char_list pop 값) 추가 검증
            get_char(char_list, str + temp_val)
    else:
        # 사전에 없는값이 나왔으므로 마지막 키값으로 저장
        index_dic[str] = index
        # 저장했으므로 키값 +1 (그래야 중첩이 안됨)
        index += 1
        # switch 변수 다시 초기값 0으롭 변경
        temp_check = 0
        # 임시값을 pop하여 다시 시작 ( K, KA 일 경우 KA에값은 사전에 넣었으니 A값부터 다시 시작)
        get_char(char_list, temp_list.pop())


data = "TOBEORNOTTOBEORTOBEORNOT"
# [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]

print(solution(data))
print(result_list)
print(index_dic)
print(temp_list)
