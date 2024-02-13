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
