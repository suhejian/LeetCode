class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


    def insert(self, word: str) -> None:
        node = self
        for c in word:
            c = ord(c) - ord('a')
            if not node.children[c]:
                # 该字符不存在
                node.children[c] = Trie()
            node = node.children[c]
        node.isEnd = True

    def searchPrefix(self, prefix):
        node = self
        for c in prefix:
            c = ord(c) - ord('a')
            if not node.children[c]:
                return None
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)