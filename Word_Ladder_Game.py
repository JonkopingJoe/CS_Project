words = []
with open("words_alpha.txt", 'r') as f:
    for line in f:
        if len(line) == 4:
            words.append(line.strip('\n'))

class WordNode:
    def __init__(self, word:str) -> None:
        self.word = word
        self.l1 = word[0]
        self.l2 = word[1]
        self.l3 = word[2]
        self.neighbors = []


    def get_neighbors(self):
        return self.neighbors
    
class Graph:
    def __init__(self) -> None:
        self.set_of_wordnodes = set()

    def add_word(self, new_wordnode) -> None:
        self.set_of_wordnodes.add(new_word)
        for wordnode in self.set_of_wordnodes:
            if wordnode.l1 == new_wordnode.l1 or wordnode.l2 == new_wordnode.l2 or wordnode.l3 == new_wordnode.l3:
                wordnode.add_neighbor(new_wordnode)
                new_wordnode.add_neighbor(wordnode)
    
    def find_ladder(self, start, end):
