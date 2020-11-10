# List
# ------------------------------------------------------------
temp_list = [3, 1, 5, 6, 4]
print(temp_list)  # [3, 1, 5, 6, 4]
# 정렬
temp_list.sort()
print(temp_list)  # [1, 3, 4, 5, 6]
# 역정렬
temp_list.reverse()
print(temp_list)  # [6, 5, 4, 3, 1]

temp2_list = ["test", "test2"]
# addAll
temp_list.extend(temp2_list)
print(temp_list)  # [6, 5, 4, 3, 1, 'test', 'test2']
# ------------------------------------------------------------


# 사전 Key, Value
# ------------------------------------------------------------
temp_dic = {3: "test1", 10: "test2", 2: "test5"}
print(temp_dic[3])
print(temp_dic[10])
print(temp_dic.get(3))
print(temp_dic.get(10))

print(temp_dic.get(5))  # 없으면 None 출력
# print(temp_dic[5])      # 없으면 예외발생
print(temp_dic.get(5, "test3"))

# Delete
del temp_dic[3]
print(temp_dic)

# KeySet
print(temp_dic.keys())

# Value
print(temp_dic.values())

# Key + Value
print(temp_dic.items())

# Clear
temp_dic.clear()
print(temp_dic)
# ------------------------------------------------------------

# Tuple - Static같은 느낌?
# ------------------------------------------------------------
temp_tuple = ("test1", "test2")
print(temp_tuple[0])

# temp_tuple.add("test3")     # 'tuple' object has no attribute 'add'
(data_a, data_b, data_c) = ("a1", "b1", "c1")
print(data_a, data_b, data_c)
# ------------------------------------------------------------

# Set - 집합
# 중복 안됨, 순서가 없음
temp_set = {1, 2, 4, 5, 3, 1}
print(temp_set)

java_set = {"test1", "test2"}
python_set = {"test1", "test3"}

# 교집합
print(java_set & python_set)
print(java_set.intersection(python_set))

# 합집합
print(java_set | python_set)
print(java_set.union(python_set))

# 차집합
print(java_set - python_set)
print(java_set.difference(python_set))

# add
python_set.add("test4")
print(python_set)

# delete
python_set.remove("test4")
# ------------------------------------------------------------

# 자료 구조 변경
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# Quiz
from random import *

users = range(1, 21)
print(type(users))
users = list(users)
print(type(users))
print(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print(f"1 >> {winners[0]}")
print(f"2,3,4 >> {winners[1:4]}")

# For
for temp_no in range(5):
    print("test num {0}".format(temp_no))

# while
no = 10
while no > 0:
    print("{0} no".format(no))
    no -= 1

# continue
temp_no = [2, 3, 5]
for no in range(1, 20):
    if no in temp_no:  # = temp_no.contains(no)
        continue
    else:
        print("포함되어있지 않는 숫자 {0}".format(no))
        break

# 한줄 for
temp_no = [1, 2, 3, 4, 5]
print(temp_no)
temp_no = [i + 100 for i in temp_no]
print(temp_no)

temp_nm = ["test", "2lkdjfdsljf", "elfje"]
print([len(i) for i in temp_nm])


# method
# 파이썬은 멀티 리턴도 되고, 애초에 함수에서 없으면 디폴트가 가능..
def test(str1, str2="default"):
    str1 += "g"
    str2 += "h"
    return str1, str2


temp_string1, temp_string2 = test("ggg", "zzz")
print("temp1 {0}, temp2 {1}".format(temp_string1, temp_string2))


temp_string1 = test("ggg")
print("temp1 {0}, temp2 {1}".format(temp_string1, temp_string2))

