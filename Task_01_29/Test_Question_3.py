from Question_3 import DynamicArray
import random


def changeToList(array_l):
    new_ar = []
    for numb in range(0, len(array_l)):
        new_ar.append(int(array_l[numb]))
    return new_ar

testArray = DynamicArray()

#test Empty array created
print(testArray._len())
print(testArray._get(0))

#insert multiple random number

for number in range(1, 21):
    number = random.randint(1, 51)
    testArray.add(number)

print("\n=== Test Length and first element ===")
print(testArray._len())
print(testArray._get(0))

#test contains method
print("\n=== Test contains method ===")
first = testArray._get(0)
print(testArray.contains(first))
print(testArray.contains(100))

print("\n=== Test reverse list ===")
new_list = testArray.reverse()
new_list = changeToList(new_list)

print("List : ", testArray)
print("Reverse: ", new_list)

print("\n=== Test insert at the begining ===")
print("Old List : ", testArray)
testArray.insert(10, 0)
print("New List : ", testArray)

print("\n== Test insert in the middle ===")
print("Old List : ", testArray)
testArray.insert(10, 10)
print("New List : ", testArray)

print("\n== Test insert at the end ===")
print("Old List : ", testArray)
testArray.insert(10, testArray._len() - 1)
print("New List : ", testArray)

print("\n== Test insert out of range ===")
print("Old List : ", testArray)
testArray.insert(10, 100)
print("New List : ", testArray)