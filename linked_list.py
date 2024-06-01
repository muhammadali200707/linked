class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Error")
        else:
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return "You don't have head that's why your new data will be your head!"
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def check(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            if last.next == new_node:
                return last.next
            last = last.next


""" THIS IS FIRST VERSION
a = Node(90)
b = Node(1)
c = Node(87)

linked_list = LinkedList()
linked_list.head = a
a.next = b
b.next = c

# print(linked_list.push(4))  # This will be new head!
# print(linked_list.insert(c, 123))  # This insert data after prev node!
# print(linked_list.append(88))  #This append data to end!
# print(linked_list.print_list())  # This prints lists!"""

"""THIS IS SECOND VERSION OF CREATING NODE --> 
linked_list = LinkedList()

data = []
for i in range(1, 20):
    data.append(i)

linked_list.head = Node(data[0])
for x in data[1::]:
    linked_list.append(x)

# linked_list.append(9) #This append data to end!
# print(linked_list.push(4))  # This will be new head!
# print(linked_list.print_list())  # This prints lists!"""

