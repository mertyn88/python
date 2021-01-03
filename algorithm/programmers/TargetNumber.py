# https://programmers.co.kr/learn/courses/30/lessons/43165

# n개의 음이 아닌 정수가 있습니다.
# 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

"""
해당 문제는 dfs를 이용하여 해결하려 했으나 너무 많은 loop와 경우의 수로
실패하고 다른사람의 답안을 보았지만 여전히 100% 이해할 수 없었다.
"""


def solution(numbers, target):
    tree = [0]
    for num in numbers:
        sub_tree = []
        for tree_num in tree:
            sub_tree.append(tree_num + num)
            sub_tree.append(tree_num - num)
        tree = sub_tree
        print(tree)
    return tree.count(target)


data_list = [1, 1, 1, 1, 1]
print(solution(data_list, 3))
