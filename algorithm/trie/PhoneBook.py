# https://programmers.co.kr/learn/courses/30/lessons/42577

"""
 Trie 알고리즘을 구성 후 문제를 해결한다.가
 일반적인 Trie구조로 찾기 시작하면 효율성 문제에서 시험을 통과할 수 없다.


"""


class Node:
    def __init__(self, text):
        self.text = text
        self.possible_word = 0
        self.data = ""
        self.child = {}


class Trie:
    def __init__(self):
        self.root = Node(None)
        self.custom_result_dic = []

    def insert(self, text):
        curr_node = self.root

        for char in text:
            if char not in curr_node.child:
                # 없으면 추가
                curr_node.child[char] = Node(char)
            # 노드 이동
            curr_node = curr_node.child[char]
            # 겹치는 단어 개수 증가
            curr_node.possible_word += 1
        # 마지막 단어 체크
        curr_node.data = text

    # 기본 search 구현
    def search(self, text):
        curr_node = self.root
        for char in text:
            if char in curr_node.child:
                curr_node = curr_node.child[char]
            else:
                return False

        # 마지막 글자까지 왔는데 data값이 있으면 True
        if curr_node.data is not None:
            return True

        return False

    # 풀이용 전용 search
    # 접두어가 없어야 True 반환
    # 하나의 단어가 끝날때까지 posibble_word의 개수가 2인것이 있으면 접두어가 존재한다.
    def solution_search(self, phone_book):
        for text in phone_book:
            # Node Root값 설
            curr_node = self.root
            for char in text:
                # 자신의 단어들끼리 순환 Loop하기 때문에 child의 값이 있는지 없는지 여부는 체크할 필요가 없다.
                # 단어 끝의 노드까지 이동
                curr_node = curr_node.child[char]

            # 마지막 노드값의 possible_word 값 확인
            if curr_node.possible_word > 1:
                return False

        # 전체 단어를 찾아도 possible_word 2이상인 값이 없으면 접두어가 존재하지 않는다.
        return True


def solution(phone_book):
    # Trie를 이용한 풀이였으나... 효율성 시간 테스트에서 탈락해서 다른 방안으로 모
    # 삽입
    # trie = Trie()
    # [trie.insert(phone) for phone in phone_book]
    # answer = trie.solution_search(phone_book)

    start_check_char = "_"
    string_book = start_check_char+"_".join(phone_book)
    print(string_book)
    for book in phone_book:
        if string_book.count(start_check_char+book) > 1:
            return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["113", "44", "4544"]))
