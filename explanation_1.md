A least Recently Used Cache(LRU Cache) is a cache that removed the least recently used entry when teh cache reaches its limit. It is used for   temporary memory storage.
Double linkedlist is the data structure used for the LRU Cache because can be updated or depleted(removed) from both ends. That is the cache can be updated or deleted from both ends of the list. A stack or queue is limited in this regard.
The time complexity is Linear O(n) because of the Single for loop in the "set(self, key, value)" function of the LRU_Cache(object) class. This means the algorithm increases or decreases with the number of inputs.