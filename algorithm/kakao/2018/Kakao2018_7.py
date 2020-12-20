# https://programmers.co.kr/learn/courses/30/lessons/17685

# trie 알고리즘
"""
    해당 문제는 Trie알고리즘을 모른채 시작되었고, 결국 해결하지 못하였다.
    Trie 알고리즘에 대한 소스를 먼저 파악한 뒤, 똑같이 타이핑을 하였고, 실제 답을 그대로 하지않고
    나만의 풀이 로직을 추가하여 해결하였다.
    풀이 로직은 search함수, 실제 문제해결은 text_search함수
"""


class Node:
    def __init__(self, text):
        # 문자
        self.text = text
        # 마지막 전체 단어
        self.data = ""
        # 중복되는 char, go, guild, gone의 경우 g는 3
        self.possible_word = 0
        # 자식 노드, dic 형태
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, text):
        curr_node = self.root
        for char in text:
            if char not in curr_node.children:
                # 해당 노드가 char가 아니면..
                curr_node.children[char] = Node(char)
            # 노드 이동
            curr_node = curr_node.children[char]
            # 겹치는 단어의 개수 표현
            curr_node.possible_word += 1
        # 마지막 노드일 경우 전체 글자를 저장한다.
        curr_node.data = text

    def search(self, text):
        curr_node = self.root
        for char in text:
            if char in curr_node.children:
                # char값이 있으면 다음노드로 설정
                curr_node = curr_node.children[char]
            else:
                return False
        # 해당 노드 까지 왔ㄷ을 때 만들 수 있는 문자의 개수가 1이면 True 반환
        if curr_node.possible_word == 1:
            return True
        else:
            return False

    def text_search(self, text):
        result_cnt = 1
        curr_node = self.root
        for char in text:
            # 첫시작이 root 노드이므로 비교되어야하는 노드는 한가지 하위 노드
            if curr_node.children[char].data == text:
                return result_cnt
            elif curr_node.children[char].possible_word == 1:
                return result_cnt
            else:
                # 아닐시 하위노드로 변환
                curr_node = curr_node.children[char]
                result_cnt += 1


def solution(words):
    tri = Trie()
    [tri.insert(word) for word in words]
    answer = sum([tri.text_search(word) for word in words])
    return answer

# data_list = ["go", "gone", "guild"]
data_list = ["word", "war", "warrior", "world"]
print(solution(data_list))
