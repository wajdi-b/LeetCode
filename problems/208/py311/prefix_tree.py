class TrieNode:
    def __init__(self, c=None):
        self.links = []
        self.is_end = False
        self.c = c

    def has_link(self, c):
        for n in self.links:
            if n.c == c:
                return True
        return False

    def get_link(self, c):
        for n in self.links:
            if n.c == c:
                return n
        return False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if node.has_link(c):
                node = node.get_link(c)
                continue
            new_node = TrieNode(c)
            node.links.append(new_node)
            node = new_node
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if node.has_link(c):
                node = node.get_link(c)
                continue
            else:
                return False
        return node and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if node.has_link(c):
                node = node.get_link(c)
                continue
            else:
                return False
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
