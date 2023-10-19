class TrieNode:
    def __init__(self):
        # Nodes that connect to children nodes
        self.children = {}

class WordDictionary:
    def __init__(self):
        # Pointer to beginning of our data struct
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        # Loop through word
        for c in word:
            # Node does not exist yet so create it
            if c not in node.children:
                node.children[c] = TrieNode()
            # Move to next node
            node = node.children[c]

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c == ".":
                # Only one possible key we could be
                if len(node.children.keys()) == 1:
                    blank_letter = list(node.children.keys())[0]
                    node = node.children[blank_letter]
                # Multiple keys so we need to search for the best one
                elif len(node.children.keys()) > 1:
                    blank_letter = list(node.children.keys())[0]
                    node = node.children[blank_letter] 
                else: 
                    return False 

            elif c in node.children:
                node = node.children[c]
            else:
                return False
        return True


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)ggh