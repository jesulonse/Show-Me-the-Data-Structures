Hoffman code is used for file compression. It is a lossless data compression algorithm in that there is no loss of information.
It involves encoding and decoding. The encoding enables the data to be compressed into a smaller size and it can be decoded back to its original size.
A binary tree is the data structure that is used because to traverse each of the characters of the data as it encodes it down the tree.

Time Complexity Analysis:

The time complexity is linearithmic: O(nlogn).Using a heap to store the weight of each tree, each iteration requires O(logn) time to determine the cheapest weight and insert the new weight. There are O(n) iterations, one for each item.
Note that at least one of the operations of insertion(addition), finding the minimum, or deleting it from a Priority Queue is O(log n).
Also the merge sort used worst case scenerio has a time complexity of O(n).
Since we are considering the worst case scenerio, therefore, the time complexity is O(nlogn).

Space Complexity Analysis:

The space complexity is linear O(n) where n is the number of nodes of tree. The more the tree nodes, the more space occupied in memory has
the tree is being created and this is the same for the decoding as it travserse the tree in linear path: O(n).

