# Define a class called Router. Each router has a model name, a software version, and an IP
# address for management. When an instance of this class is created, the value to these fields
# are passed into the __init__ method. 
class Router(): 
    @classmethod

    def __init__(self, modname, ver, address):
        self.modname = modname
        self.ver = ver
        self.address = address
    
    def rdetails(self):
        print(f"Details: (name), (ver), (address)")
        print(f"Details: {self.modname}, {self.ver}, {self.address}")
    



# Once completed, we can create an instance of Router.
router1 =  Router("v64", "0.2", "10.0.0.1")

# write code to print the details of the router

router1.rdetails()