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

    def get_friends(self, member:Member) -> list:
        """
        Get the list of friends for a given person.

        Args:
            member (Member): The instance of a member.

        Returns:
            list: A list of friends' name

        Usage:
            bikiniBottom.get_friends(spongeBob)
        """
        friends = []
        if member in self.set_of_members:
            for friend in member.friends_list:
                friends.append(friend.name)
            return friends
        else:
            return None
    def shortest_path(self, start:Member, end:Member) -> int:
        """
        Get the degree of shortest path between two members
        !!!Notice: receive instances of class Member, not name!!!
        
        Arg:
            start(member)
            end(member)

        Return:
            int: The degree (length) of the shortest path

        Usage:
            bikiniBottom.shortest_path("spongeBob", "patrick")
        """
        if start == end:
            return 0
        queue = [start]    #a queue with members waiting to be checked
        visited = set()    #a set which store members have been searched
        distance = {start: -1}    
        #record our counting
        #notice the first time we seach for starting member itself, distance+=1 should be 0, so we start with -1
        while queue:    #always true
            current = queue.pop(0)    #get the item to compare
            if current == end:    #if it is the target
                return distance[current]+1    #get the distance
            visited.add(current)    #store members with are not the target
            for friend in current.friends_list:    #traverse the edges of current member
                if friend not in visited:
                    queue.append(friend)    #add friends of current member to the queue waiting to be checked
                    distance[friend] = distance[current] + 1
        return None    #default
