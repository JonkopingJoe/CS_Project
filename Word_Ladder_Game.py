#  Function to load the words we need from the database
def load_all_words(file_name: str) -> list:
    with open("words_alpha.txt", 'r') as f:
        words = []
        for line in f:
            if len(line) == 4:
                words.append(line.strip('\n'))
    return words

# Function to find neighbours from the list of words we have extracted from Db
def find_neighbours(word, words) -> list:
    """
    Finds the neighbours in the word list

    Args: 
    - A word  
    - List of words from the database

    Returns: 
    A list of all words in the database that can be formed by changing the one letter in the input word
    """  
    neighbours = []
    for a_word in words:
        if len(a_word) == word:
            # Find the positions where word and a_word have different letters and flag as True or False
            # Count the True values to count the pairs of characters different between two the words
            
            diff_count = sum(a != b for a,b in zip(word, a_word))
            if diff_count == 1:
                # if there is only 1 difference between the word and a word in the Db
                neighbours.append(a_word)
            return neighbours


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
