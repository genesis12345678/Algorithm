import sys

input = sys.stdin.readline


class Node(object):
    def __init__(self, isEnd):
        self.isEnd = isEnd
        self.childNode = [None] * 26  # 알파벳 개수만큼 크기 생성


class Trie(object):
    def __init__(self):
        self.parent = Node(None)  # Trie가 생성될 때 루트 노드 설정, 루트 노드는 공백이므로 None

    def insert(self, string):
        nowNode = self.parent  # 루트 노드

        for char in string:  # 입력 문자열을 돌면서 진행
            index = ord(char) - ord('a')  # 현재 문자의 index

            if nowNode.childNode[index] is None:  # 문자가 아직 생성된 적이 없다면 새로 생성
                nowNode.childNode[index] = Node(False)

            nowNode = nowNode.childNode[index]  # 다음 자식 노드로 이동

        nowNode.isEnd = True  # 마지막 자식 노드에 마지막임을 표시

    def search(self, string):
        nowNode = self.parent  # 루트 노드

        for char in string:
            index = ord(char) - ord('a')

            if nowNode.childNode[index] is None:  # 자식 노드에 찾고자 하는 문자가 없으면 False 반환
                return False
            nowNode = nowNode.childNode[index]  # 다음 자식 노드로 이동

        return nowNode.isEnd  # 마지막 문자 여부를 반환


n, m = map(int, input().split())
trie = Trie()  # Trie 생성

for _ in range(n):
    word = input().strip()  # strip(): 문자열 양 끝 공백 제거
    trie.insert(word)

result = 0

for _ in range(m):
    word = input().strip()
    if trie.search(word):
        result += 1

print(result)
