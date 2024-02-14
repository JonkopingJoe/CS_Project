class Node:
    def __init__(self, name: str, age: int, location: str):
        self.name = name
        self.age = age
        self.location = location
        self.friends_list = []  # Holds nodes in the graph class

    def add_friend(self, new_friend) -> None:  # Makes new edge
        if new_friend not in self.friends_list:
            self.friends_list.append(new_friend)

        return None


class Graph:
    def __int__(self):
        self.set_of_nodes = set()

    def add_node(self, node: Node) -> None:
        if node not in self.set_of_nodes:
            self.set_of_nodes.add(node)

        return None

    def add_relations(self, person1: Node, person2: Node) -> None:
        if person1 in self.set_of_nodes and person2 in self.set_of_nodes:
            person1.add_friend(person2)
            person2.add_friend(person1)

        return None

    def get_friends(self, name: str) -> list:
        for person in self.set_of_nodes:
            if person.name == name:
                return person.friends_list

        return None
