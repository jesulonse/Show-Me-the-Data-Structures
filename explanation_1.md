A least Recently Used Cache(LRU Cache) is a cache that removes the least recently used entry when the cache reaches its limit. It is used for   temporary memory storage.
Double linkedlist along side a hash map is the data structure used for the LRU Cache because it can be updated or depleted(removed) from both ends. That is the cache can be updated or deleted from both ends of the list. A stack or queue is limited in this regard.

Time complexity Analysis:

LRU cache store items in order from most-recently used to least-recently used. That means both can be accessed in O(1) time. The time complexity is derived from the double linkedlist that is constant time O(1). 
Also each time an item is accessed, updating it takes O(1). That is super fast.
But in the worst case scenerio, the "for" loop found in line 126 for updating the dictionary "self.item_dict", this made the time complexity linear O(n).
Therefore, the time complexity for the least Recently Used Cache(LRU Cache) is linear: O(n).

Space Complexity Analysis:

Least Recently Used Cache(LRU Cache) takes a lot of space as an LRU cache tracking "n" items requires a double linkedlist of length "n", and a hash map holding "n" items. That is O(n) space for both data structures, double linkedlist and hash maps, that is used to store the items
