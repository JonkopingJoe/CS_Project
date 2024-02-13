#First project
#Social Network Graph

class Graph:
    def __init__(self):
        self.members = {}
        #Create a dictionary to store members as Nodes
        self.relationships = {}
        #Create a dictionary to store relationships as Edges
    
    def add_member(self, member: str, **kwargs):
        if member not in self.members:
        #Check if the member exists
            self.members[member] = kwargs
            #Create a new member with the kwargs
            self.relationships[member] = []
            #Create relationships for the member

    def find_friends(self, member: str):
        """
        This method finds all the friends of a particular member.

        Args:
        - member: this is the Name of the member

        Returns:
        - List of all the member's friends

        Usage:
        print("Friends of Alice:", social_network.find_friends("Alice"))
        """
        if member in self.members:
            return self.relationships[member]
        else:
            return []
    