class Node:
    def __init__(self, val = None, isEnd = False):
        self.val = val
        self.children = dict()
        self.isEnd = isEnd
        

class Trie:
    def __init__(self):
        self.root = Node(None, False)

    def insert(self, string):
        cur = self.root
        for i in range(len(string)):
            char = string[i]
            if i < len(string) - 1:
                if char in cur.children:
                    cur = cur.children[char]
                else:
                    cur.children[char] = Node(char, False)
                    cur = cur.children[char]
            else:
                if char in cur.children:
                    newnode = Node(True)
                    cur = cur.children[char]
                    cur.children[''] = Node('', True)
                else:
                    cur.children[char] = Node(char, False)
                    cur = cur.children[char]
                    cur.children[''] = Node('', True)

    def search(self, string):
        cur = self.root
        for i in range(len(string)):
            char = string[i]
            if char not in cur.children:
                return False
            cur = cur.children[char]
            if i >= len(string) - 1:
                if '' in cur.children:
                    return True
                else:
                    return False
        return False
    
    def startsWith(self, string):
        cur = self.root
        for i in range(len(string)):
            char = string[i]
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
