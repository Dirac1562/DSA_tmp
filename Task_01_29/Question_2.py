import numpy as np
from Question_1 import Array

# Question
# Create a dynamic array subclass which also has the following basic methods:
# a. add(val) which adds an element to the end
# b. del() which removes the last element of the array

# the first thing we should do is create an array using numpy
# this is the array we'll be using to test out our function
# i am using numpy and its append and del methods

class DynamicArray(Array):

# this method adds an element to the end of the array using the numpy function append, which automatically creates a
# new array with the new element as the last element
# this is done because the size of an array is immutable, so this is a way around that
    def add_end_element(self, value):
        """ Add an new element at the end of the list""" 
        if self.array is not None:
            # use numpy append method to add an element
            self.array = np.append(self.array, value)
            print(">>> A new element was succesfullly added")
        else:
            print(f">>> [value] : {value} was not added in the list")


# this method removes the element at the end of the array using the numpy function delete, which automatically creates
# a new array without the last element
# this is done because the size of an array is immutable, so this is a way around that
    def remove_end_element(self):
        if self.array is not None and self._len() > 0:
            self.array = np.delete(self.array, -1)
            print(">>>The last element was succesfully deleted")
        else:
            print(">>>The last element was not deleted")

