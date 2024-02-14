#First project
#Social Network Graph

class Graph:
    def __init__(self):
        #Create a dictionary to store members as Nodes, names as keys, values are dics with ages and locations.
        #Example: {"Joe":{"age": 21, "Location": "Coventry"}
        self.members = {}
        #Create a dictionary to store relationships as Edges
        #Members as keys, and lists to store relationships
        #Example: {"Joe":["Xi Jingping", "Kim Jung-un"]
        self.relationships = {}
    
    def add_member(self, member: str, **kwargs):
        """
        This method add a new member into the graph

        Args:
        - member: a str as name of member, stored as a key in dic members
        - age: a nember as age of member
        - location: a str as the location for member

        Return:
        -None
        
        Usage:
        network.add_member("Joe", age=21, location="Coventry")
        """

    def add_relationship(self, name1, name2):
        if name1 not in self.relationships[name2] and name2 not in self.relationships[name1]:
            self.relationships[name1].append(name2)
            self.relationships[name2].append(name1)
        else:
            print("Both users are already friends")

    def find_friends(self, member: str):
        """
        This method finds all the friends of a particular member.

        Args:
        - member: this is the Name of the member

        Returns:
        - A list of all the member's friends

        Usage:
        print("Friends of Alice:", social_network.find_friends("Alice"))
        """
        if member in self.members:
            return self.relationships[member]
        else:
            return []
    
