"""
File: BSTdict.py
Implement dictionary using binary search trees.
"""

from bst import BST
        
class BSTtreeDict(BST):
    '''A BST-based implementation of a sorted dictionary'''
    def __init__(self):
       
        self._items = BST()
    
    def __getitem__(self,key):	
    	'''Returns the value associated with key or returns None if key does not exist.'''
        return self._items.find(key)

    def __setitem__(self, key, value):
    	self._items.add((key, value))
           
    def __contains__(self,key): 
        return self.__getitem__(key) != None

    def __str__(self):
        return str(self._items) 

    def __len__(self): 
        return len(self._items)   

    def __iter__(self): 
        return iter(self._items)

    def pop(self,key): 
        return self._items.remove(key) 
        



def main():
    tree = BSTtreeDict()
    
    tree['G'] = 6
    tree['H'] = 16
    tree['A'] = 60
    # tree.addVal('C',260) 
    # tree.addVal('C',269)
    # tree.addVal('C',9) 
    tree['C'] = 60
    tree['C'] = 36
    tree['E'] = 3
    tree['F'] = 50
    tree['J'] = 5
    tree['J'] = 15
    
    print "\nTree:\n" + str(tree)

   
    print "Find:", " -> ", tree.__getitem__('A')
    print "Find:", " -> ", tree['C']
    print "\nTree:\n" + str(tree)
    for item in tree:
        print item,


if __name__ == "__main__":
    main()
    
