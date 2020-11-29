# https://programmers.co.kr/learn/courses/30/lessons/17677
import re
import math
from collections import Counter


def solution(str1, str2):
    str_list1 = divide_str(str1)
    str_list2 = divide_str(str2)

    # num1 = len(Counter(str_list1) & Counter(str_list2))
    num1 = len(list((Counter(str_list1) & Counter(str_list2)).elements()))
    num2 = len(list((Counter(str_list1) | Counter(str_list2)).elements()))

    if num1 == 0 and num2 == 0:
        return 65536
    else:
        answer = math.trunc((num1 / num2) * 65536)

    return answer


def divide_str(str):
    # france
    temp_list = list(str)
    temp_list2 = []

    for index in range(len(temp_list)):
        # f r a n c e
        if index < len(temp_list) - 1:
            regex_str = temp_list[index].lower() + temp_list[index + 1].lower()
            if bool(re.match("[a-z]{2}", regex_str)):
                temp_list2.append(regex_str)

    return temp_list2
