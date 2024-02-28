### About this repository  

These are implementations of mini projects assigned to us (collaborators of this repository) during DSA classes.  
Probably not *"the next big thing"* at the moment, we thought you should know.    

#### Details of the Mini Projects  

1. Network Connectivity  
   **Prompt**: You must implement a graph representing a list of connections between computers in a network, represented as lists [a, …, n] where a to n are the IDs of two or more connected computers. Your task is to determine if the entire network is connected. 
   Write a Graph class that allows you to add and remove a graph vertex (each vertex represents a computer in the network) and define the edges between vertices (an edge represents the connection between computers). Implement an adjacency matrix to define these connections. Write a function which outputs this matrix.  
   Write a function is_network_connected that returns a bool value. The function parameter can be the graph containing the vertices representing the computers in the network. It returns a boolean value indicating if the entire network is connected, i.e., it returns True if each computer has at least one connection.  
   Hint: You can use graph traversal algorithms (e.g., depth-first search or breadth-first search) to explore the connected components of the network. If you can traverse all vertices in the graph, that means all computers are connected.

2. Social Network Graph  
   **Prompt:** Build a social network graph using graph data structures. You will create a program that allows users to add new members to the network and define relationships between members. The program should be able to answer questions about the social network, such as who is friends with whom and how many degrees of separation there are between two members.

3. Word Ladder Game  
   A word ladder is a game where you try to transform one word into another by changing
   one letter at a time. For example, you can transform the word “CAT” into the word “DOG”
   using the following sequence of words:
   CAT -> COT -> DOT -> DOG

   For this project, create a program to find the shortest word ladder between two given words. 
   To do this, first, import a list of possible words from the English language word database (words_alpha.txt).  
   Secondly, define a function called find_neighbors that takes one word and a list of words (from the words_alpha file) as input and returns a list of all the words in the list that can be formed by changing one letter in the input word. For example, if the input word is “CAT” and the list of words contains the words “COT”, “BAT”, and “RAT”, then the output of the find_neighbors function should be [“COT”].  
   Next, define a function called word_ladder that takes a start word and an end word as input and uses the find_neighbors function to find the shortest path between the start and end word. For this purpose, use a breadth-first search (BFS) algorithm; start by adding the start word to a queue, along with an empty path. Then dequeue a word from the queue and use the find_neighbors function to find all the neighbours of that word. If any of the neighbours is the end word, return the path built up to that point. Otherwise, add each neighbour to the queue along with the path so far. Continue this process until finding the end word or until the queue becomes empty.
