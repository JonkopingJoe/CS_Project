class Member:
    def __init__(self, name: str, age: int, location: str):
        """
        Initialize a Member object with a name, age, and location.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            location (str): The location of the person.
        Usage:
            spongeBob = Member("SpongeBob SquarePants",35,PeanappleHouse)
        """
        self.name = name
        self.age = age
        self.location = location
        self.friends_list = [] # Holds members in the graph class

    def add_friend(self, new_friend) -> None:  # Makes new edge
        """
        Add a new friend to the member's friends list, to abstract an edge

        Args:
            new_friend (Node): The node representing the new friend to connect.

        Returns:
            None

        Usage:
            spongeBob.add_friend(patrick)
        """
        if new_friend not in self.friends_list:
            self.friends_list.append(new_friend)

        return None


class Graph:
    """
    Initialize an empty graph.
    """
    def __init__(self):
        self.set_of_members = set()

    def add_member(self, member: Member) -> None:
        """
        Add a node to the graph.

        Args:
            member (Member): The node to be added to the graph, an instance of class Member.

        Returns:
            None

        Usage:
            bikiniBottom.add_member(spongeBob)
        """
        if member not in self.set_of_members:
            self.set_of_members.add(member)

        return None

    def add_relations(self, person1: Member, person2: Member) -> None:
        """
        Add a relation between two members in the graph, representing an edge.

        Args:
            person1 (Node): The first node, an instance of class Member.
            person2 (Node): The second node, an instance of class Member.

        Returns:
            None

        Usage:
            bikinibottom.add_relations(spongeBob, patrick)
        """
        if person1 in self.set_of_members and person2 in self.set_of_members:
            person1.add_friend(person2)
            person2.add_friend(person1)

        return None

    def get_friends(self, name: str) -> list:
        """
        Get the list of friends for a given person.

        Args:
            name (str): The name of the person.

        Returns:
            list: A list of friends' Node objects, or None if the person is not found.

        Usage:
            bikiniBottom.get_friends(spongeBob)
        """
        for person in self.set_of_members:
            if person.name == name:
                return person.friends_list

        return None
