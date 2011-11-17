#
# Jasy - Web Tooling Framework
# Copyright 2010-2011 Sebastian Werner
#

__all__ = ["Formatting"]


class Formatting:
    """
    Configures an formatting object which can be used to compress classes afterwards.
    The optimization set is frozen after initialization which also generates the unique
    key based on the given formatting options.
    """
    
    __allowed = ("wrap", "declarations", "blocks", "variables", "privates")
    
    
    def __init__(self, *args):
        self.__formatting = set()
        
        for identifier in args:
            if not identifier in self.__allowed:
                logging.warn("Unsupported formatting option: %s", identifier)
                
            self.__formatting.add(identifier)
            
        self.__key = "+".join(sorted(self.__formatting))
        
        
    def getKey(self):
        """
        Returns a unique key to identify this formatting set
        """

        return self.__key


    # Map Python built-ins
    __repr__ = getKey
    __str__ = getKey        