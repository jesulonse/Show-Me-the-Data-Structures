class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
#Double linkedlist is used as cache can be depleted from both ends
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

       
    def append(self, value):
        """ Append a node to the end of the list """
        #since the head is None, then the head equals the tail meaning there is only one element in the list which is None
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

       
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
       
   
    def prepend(self, value):
        """ Prepend a node to the beginning of the list """
        #since the head is None, then the head equals the tail meaning there is only one element in the list which is None
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        new_head = DoubleNode(value)
        #the next head to the new head is the self.head
        new_head.next = self.head
        #the self.head is now the new_head that has been prepended to it
        self.head = new_head
        #the previous item of the next head is the self.head as new items are prepended to it from the front
        self.head.next.previous = self.head
       

     
       
    def remove_node(self, value):
        """ Delete the first node with the desired data. """
        node = self.head
       
        if node is None:
            return
        elif node.value == value:
            self.remove_head()
        elif self.tail.value == value:
            self.remove_tail()
        else:
            while node:
                if node.value == value:
                    #when the value at the node is removed, the next element to previous element is the next element to the node
                    node.previous.next = node.next
                    #the item to is previous to the next node is the previous item to the node
                    node.next.previous = node.previous
                #node becomes the next node since the item at the node has been removed    
                node = node.next
           
   
    def remove_head(self):
        if self.head is None:
            return
       
        #there is no more item at the head position once it has been removed, hence return that at the next position
        self.head = self.head.next
        self.head.previous = None
   
    def remove_tail(self):
        if self.tail is None:
            return
       
        #there is no more item at the tail position once it has been removed, hence return that at the previous position
        self.tail = self.tail.previous
        self.tail.next = None
       
       
       
   
   
class LRU_Cache(object):
       

    def __init__(self, capacity = 5):
        # Initialize class variables
        self.num_entries = 0
        self.capacity = capacity
        self.item_dict = dict()
        self.cache = DoublyLinkedList()
        if self.capacity < 5:
            print('cache size cannot be less than 5 items')


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.item_dict:
            return -1
        #Retrieve item using the unique key
        value = self.item_dict[key].value
        #remove the item using the key
        self.cache.remove_node(value)
        #prepend the removed value to the dictionary top
        self.cache.prepend(self.item_dict[key])
        #return the value
        return value
       

    def set(self, key, value):
        # Set the value if the key is not present in the cache  
        if key not in self.item_dict:
            #and the cache capacity is not full.
            if self.num_entries < self.capacity:
                self.cache.prepend(value)
                self.item_dict[key] = self.cache.head
                self.num_entries += 1
            else:
            #If the cache is at capacity(full)  
                #initializing the least used key as None
                least_used_key = None
                for key, item in self.item_dict.items():
                    #the least used key is usually at the tail
                    if item.value == self.cache.tail.value:
                        least_used_key = key
                #remove the oldest item(least used item)        
                self.cache.remove_tail()
                self.item_dict.pop(least_used_key)

                #and add the new item after it.
                self.cache.prepend(value)
                self.num_entries += 1
           
       

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

#Edge cases
#checking for values present in the cache
our_cache.get(1)       
our_cache.get(2)       
print(our_cache.get(1)) # returns 1
print(our_cache.get(2)) # returns 2

#checking for values not present in the cache
our_cache.get(11)      
print(our_cache.get(11)) # returns -1 because 11 is not present in the cache

#adding new values to the cache to make it exceed capacity of the cache
our_cache.set(5, 5)
our_cache.set(6, 6)

#checking for the least used cache
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))

#checking for repeated values to see that the program works for a continuously used value or item of the cache
our_cache.get(1)
our_cache.get(2)
print(our_cache.get(1)) #returns 1
print(our_cache.get(2)) #returns 2 Meaning that once the item is continously used in the cache, it will remain in cache

#Negative, null values
our_cache.get(-20)
print(our_cache.get(-20)) #returns -1 whether it is Null or negative value provided it is not in the cache when the cache is of full capacity
our_cache.get("")
print(our_cache.get(""))