from collections import deque

q = deque()

# enqueue
q.append(5)
q.append(8)
q.append(2)

print(q)
q.popleft()
print(q)

q.appendleft(1)  # add_first
print(q)

q.append(3)  # add_last
print(q)

q.popleft()  # remove_first
print(q)

q.pop()  # remove last
print(q)


# time complexity O(1)

# Priority Queues

class My_Item:
    def __init__(self, key, element):
        self.key = key
        self.element = element

    def get_element(self):
        return self.element

    def set_element(self, element):
        self.element = element

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

# creating object
item = My_Item(10, "Task A")

# get methods
print(item.get_element())
print(item.get_key())
# modifying object attributes/ pdating object state

# set methods
item.set_element("Homework")
item.set_key(50)

# print again
print(item.get_element())
print(item.get_key())

# A generic priority queue class.

class My_Priority_Queue:

    def __init__(self):
        self.data = []

    # return number of elements
    def _size(self):
        return len(self.data)

    # check if empty
    def is_empty(self):
        return len(self.data) == 0

    # insert new item
    def insert_item(self, key, value):
        self.data.append((key, value))

    # return element with minimum key
    def min_element(self):
        minimum = min(self.data)
        return minimum[1]

    # return minimum key
    def min_key(self):
        minimum = min(self.data)
        return minimum[0]

    # remove minimum item
    def remove_min(self):
        minimum = min(self.data)
        self.data.remove(minimum)
        return minimum

pq = My_Priority_Queue()

# insert items
pq.insert_item(5,"Game")
pq.insert_item(3,"Homework")
pq.insert_item(4,"Love")

# print all data
print(pq.data)

# size
print("Size:", pq._size())

# is empty
print("Empty:", pq.is_empty())

# minimum element
print("Min element", pq.min_element())

# minimum key
print("Min key", pq.min_key())

# remove minimum
print("Removed:", pq.remove_min())

# print after remove
print("Queue now:",pq.data)

# Priority Queue
class My_Priority_Queue:

    def __init__(self):
        self.data = []

    # insert item
    def insert_item(self, key, value):
        self.data.append((key, value))

    # remove minimum
    def remove_min(self):
        minimum = min(self.data)
        self.data.remove(minimum)
        return minimum[1]


# sequence
S = [5, 1, 8, 2, 3]

# create priority queue
P = My_Priority_Queue()

print("Before:", S)

# insert elements into priority queue
for e in S:
    P.insert_item(e, e)

# clear S
S = []

# remove elements in sorted order
while len(P.data) > 0:
    S.append(P.remove_min())

print("After:", S)

class My_Priority_Queue:

    def __init__(self):
        self.data = []

    # insert item
    def insert_item(self, key, value):
        self.data.append((key, value))

    # remove minimum
    def remove_min(self):
        minimum = min(self.data) # serch the min tuple (1,1)
        self.data.remove(minimum)
        return minimum[1] # return value element, not a key[0]

    # check if empty
    def is_empty(self):
        return len(self.data) == 0


# sequence S
S = [5, 1, 8, 2]

# priority queue P
P = My_Priority_Queue()

print("Original S:", S)

# FIRST WHILE
# move elements from S to P

while len(S) > 0:

    e = S.pop(0)   # remove_first()
    P.insert_item(e, e)

    print("Inserted into P:", P.data)


# SECOND WHILE
# remove min and insert back into S

while not P.is_empty():

    e = P.remove_min()   # remove_min()
    S.append(e)          # insert_last()

    print("S now:", S)

print("Sorted S:", S)

class My_Priority_Queue:

    def __init__(self):
        # unordered sequence
        self.data = []

    # insert item O(1)
    def insert_item(self, key, value):
        self.data.append((key, value))

    # return minimum key O(n)
    def min_key(self):
        minimum = min(self.data)
        return minimum[0]

    # return minimum element O(n)
    def min_element(self):
        minimum = min(self.data)
        return minimum[1]

    # remove minimum O(n)
    def remove_min(self):
        minimum = min(self.data)
        self.data.remove(minimum)
        return minimum
