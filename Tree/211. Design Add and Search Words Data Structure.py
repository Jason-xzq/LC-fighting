class WordDictionary:

    def __init__(self):
        self.trieRoot = Trie()

    def addWord(self, word: str) -> None:
        self.trieRoot.insert(word)

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.isEnd
            if word[index] != '.':
                ch = ord(word[index]) - ord('a')
                if node.children[ch] is not None and dfs(index + 1, node.children[ch]):
                    return True
            else:
                for ch in range(26):
                    if node.children[ch] is not None and dfs(index + 1, node.children[ch]):
                        return True
            return False

        return dfs(0, self.trieRoot)


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

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)