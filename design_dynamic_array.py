"""
Design Dynamic Array (Resizable Array)
======================================
Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call void pushback(int n) but the array is full, we should resize the array first.

Example 1:

Input:
["Array", 1, "getSize", "getCapacity"]

Output:
[null, 0, 1]
Example 2:

Input:
["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

Output:
[null, null, 1, null, 2]
Example 3:

Input:
["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

Output:
[null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
Note:

The index i provided to get(int i) and set(int i) is guaranteed to be greater than or equal to 0 and less than the number of elements in the array.
"""

# solution
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None]*capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        index = None
        curr_index = 0
        print(self.array)
        while curr_index < self.capacity:
            if self.array[curr_index] is not None:
                if index is None:
                    index = 0
                else:
                    index = index + 1
                if index == i:
                    return self.array[curr_index]
                curr_index = curr_index + 1
            else:
                curr_index = curr_index + 1

        return -1

    def set(self, i: int, n: int) -> None:
        try:
            for index in range(i, len(self.array)):
                if self.array[index] is not None:
                    self.array[index] = n
                    break
        except Exception:
            return 

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.size += 1
        try:
            if self.array[-1] is None:
                self.array[-1] = n
            else:
                raise ValueError()
        except Exception:
            try:
                none_index = self.array.index(None)
                _ = self.array.pop(none_index)
                self.array.append(n)
            except Exception:
                self.array.append(n)
                self.capacity += 1

    def popback(self) -> int:
        self.size -= 1
        for index in range(self.capacity-1, -1, -1):
            if self.array[index] is not None:
                a = self.array[index]
                self.array[index] = None
                return a
        return -1

    def resize(self) -> None:
        self.capacity = 2 * self.getCapacity()
        new_array = [None]*self.capacity
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        
        self.array = new_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity