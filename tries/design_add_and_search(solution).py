class TrieNode:
    def __init__(self):
        # Nodes that connect to children nodes
        self.children = {} # a : TrieNode
        self.isEndWord = False

class WordDictionary:
    def __init__(self):
        # Pointer to beginning of our data struct
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        # Loop through word
        for c in word:
            # Node does not exist yet so create it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to next node
            cur = cur.children[c]
        cur.isEndWord = True

    def search(self, word: str) -> bool:
        # Meat and potatoes of this problem :)

        def dfs(j, root):
            cur = root
            # Do not want to start at 0 sometimes
            for i in range(j, len(word)):
                c = word[i]
                # The special fun case (recursive)
                if c == ".":
                    # ".ab"
                    # Could match any of our possible characters
                    for child in cur.children.values():
                        # Need to pass next index, and node 
                        if dfs(i + 1, child):
                            return True
                    return False
                # Normal case
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEndWord

        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)ggh