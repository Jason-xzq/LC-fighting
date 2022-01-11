class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            next_index = ord(ch) - ord('a')
            if not node.children[next_index]:
                node.children[next_index] = Trie()
            node = node.children[next_index]
        node.isEnd = True

    def searchPrefix(self, prefix: str):
        node = self
        for ch in prefix:
            next_index = ord(ch) - ord('a')
            if not node.children[next_index]:
                return None
            node = node.children[next_index]
        return node

    def search(self, word: str) -> bool:
        hasPrefix = self.searchPrefix(word)
        if hasPrefix and hasPrefix.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        hasPrefix = self.searchPrefix(prefix)
        if not hasPrefix:
            return False
        else:
            return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)