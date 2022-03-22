class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    #using a dictionary because the time complexity is linear (O(1))
    #intiating an empty dictionary
    dict = {}
   
    node = llist_1.head
    #while there is a value in the linkedlist, continue to populate the node starting from
    #the head to the next value in the empty dictionary
    while node:
        dict[node.value] = True
        node = node.next

    node = llist_2.head
    while node:
        dict[node.value] = True
        node = node.next
       
    #populating the empty list with the key of the dictionary as the eelements
    #the union of the two linkedlists
    #the key is populated into the union list instead of the value because the key is not duplicated
    #while the value can be duplicated and the key is the true value of the linkedlist
    #while the value is the frequency of the dictionary
    union_llist = []
    for key in dict:
        union_llist.append(key)
    return union_llist
   
   

def intersection(llist_1, llist_2):
    #using a dictionary because the time complexity is linear (O(1))
    #intiating an empty dictionaries to represent each linkedlist, llist_1, llist_2 respectively
    dict1 = {}
    dict2 = {}
   
    node = llist_1.head
    #while there is a value in the linkedlist, continue to populate the node starting from
    #the head to the next value in the empty dictionary
    while node:
        dict1[node.value] = True
        node = node.next

    node = llist_2.head
    while node:
        dict2[node.value] = True
        node = node.next
       
    #populating the empty list with the key of the dictionary as the eelements
    #the union of the two linkedlists
    #the key is populated into the union list instead of the value because the key is not duplicated
    #while the value can be duplicated and the key is the true value of the linkedlist
    #while the value is the frequency of the dictionary
    intersect_llist = []
    for key in dict1:
        if key in dict2:
            intersect_llist.append(key)
   
    return intersect_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]


for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
