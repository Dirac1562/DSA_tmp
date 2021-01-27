# import required classes and modules

#These functions are snippets code that will be added to the dynamic array class.

def contains(self, value):
    """ check if the array contains the value as element"""
    if self.get(value) is False:
        return False
    return True

def reverse(self, value):
    """reverse the array"""
    for 