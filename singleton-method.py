
''''
Singleton: A singleton is a creational pattern that restricts the instantiation of a class to one object, 
ensuring that only one instance of the class exists. For example,
consider a logger class that is used to write logs to a file.
'''


class Singleton:
    __instance = None
    
    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton")
        else:
            Singleton.__instance = self
            
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print(s1)
print(s2)

# Output:
# <__main__.Singleton object at 0x000001>
# <__main__.Singleton object at 0x000001>

print(s1 == s2)

# Output:
# True

"""

The time complexity is O(1) because the get_instance() method always returns the same instance of the Singleton class. 
The initialization of the Singleton instance only happens once, and subsequent calls to get_instance()
will return the same instance without any 
additional operations.
"""
