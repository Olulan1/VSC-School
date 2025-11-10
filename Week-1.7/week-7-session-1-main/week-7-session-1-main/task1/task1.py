# Define a class called Router. Each router has a model name, a software version, and an IP
# address for management. When an instance of this class is created, the value to these fields
# are passed into the __init__ method. 

class Router:

    def __init__(self, MName="", softVer="", IP="69.8.1"):
        self.MName = MName
        self.softVer = softVer
        self.IP = IP
    
    def getIP(self):
        a = self.IP
        return a
    
    def getRouterProperties(self):
        print(self.MName, self.softVer, self.IP)
    
# Once completed, we can create an instance of Router.
router1 = Router("iosV", "15.6.7", "10.10.10.1")
router2 = Router("iosV", "15.6.7")

    
# write code to print the details of the router

router1.getRouterProperties()
