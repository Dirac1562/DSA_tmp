#import class

Array = __import__("Question_1").Array

print("==== Test case initializing empty list =====")
array_1 = Array()
print(array_1)
print("Expected value : []\n")

print("==== Test case initialization =======")
array_1 = Array([1, 2])
print(array_1)
print("Expected value : [1, 2]\n")

print("=== Test case _len function ====")
print(array_1._len())
print("Expected value : 2")

print("===Test case _get function =====")
print(array_1._get(1))
print("Expected value : 2")