# Better attempt after watching part of the video

class TrieNode:
    def __init__(self):
        # Do not need to keep track of letter since the hashmap will do that
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        wordLen = len(word) - 1
        count = 0
        for e in word:
            if e not in node.children:
                node.children[e] = TrieNode()
            
            if count == wordLen:
                node.endOfWord = True
                print(node.children)
            node = node.children[e]
            count+=1


    def search(self, word: str) -> bool:
        node = self.root
        wordLen = len(word) - 1
        count = 0
        for e in word:
            if e in node.children:
                print(count, node.endOfWord)
                if count == wordLen and node.endOfWord:
                    return True
                node = node.children[e]
            else:
                return False
            count+=1
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for e in prefix:
            if e not in node.children:
                return False
            print(node.children)
            node = node.children[e]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# this was a shitty attempt

class Trie:
    root = {}
    def __init__(self, isEnd=False, next={}):
        self.isEnd = isEnd
        self.next = next


    # def addNode(self, node, isEnd = False, next = None):
       
    def insert(self, word: str) -> None:
        test = {'a': Trie()}
        test['a'].next = {'b': Trie()}
        print("test", test['a'].next['b'].next)
        node = self.root
        for e in word:
            # print("node", node)
            if node:
                # Already have node so get next node
                if e in node:
                    node = node[e].next
                # Node does not exist so create it and continue
                else:
                    node[e] = Trie()
                    node = node[e].next
            # Create dict for node
            else:
                print(e)
                node[e] = Trie()
                print("next", node[e].next)
                print("node1", node)
                node = node[e].next
                print("node2", node)
        # test = self.root
        # while test:
        #     print(list(test.keys())[0])
        #     test = test[list(test.keys())[0]].next

    def search(self, word: str) -> bool:
        return

    def startsWith(self, prefix: str) -> bool:
        return

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)