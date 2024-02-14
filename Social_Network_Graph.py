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
        #Check if the member exists
        if member not in self.members:
            #Create a new member with the kwargs(age and location) 
            self.members[member] = kwargs
            #Create relationships for the members, an empty list as default
            self.relationships[member] = []

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
    
