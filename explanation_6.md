This is to design the union and intersect function for a linkedlist
The linkedlist is first generated to empty. Then, it is populated with a list of elements.
A dictionary is used because its time complexity is linear and is used to populate a dictionary whose key is used populate the union linkedlist 
or intersect linkedlist respectively.

Time Complexity Analysis:

Union :
We populate the empty list with the key of the dictionary as the elements of the union of the two linkedlists
The key is populated into the union list instead of the value because the key is not duplicated.
while the value can be duplicated and the key is the true value of the linkedlist
NOte the value is the frequency of the dictionary

Intersect :
Populating the empty list with the key of the dictionary as the elements of the intersect of the two linkedlists
the key is populated into the intersect list instead of the value because the key is not duplicated.
while the value can be duplicated and the key is the true value of the linkedlist
while the value is the frequency of the dictionary.
The intesect is to ensure each key of the dict1 of the first linkedlist are the same (intersect) with that of the second linkedlist

The time complexity for the linkedlist is linear O(n).
The time complexity for the dictionary is constant O(1) in both union and intersect.

Time complexity of Union:
linkedlist a has O(a) 
linkedlist b has O(b)
Therefore, the union is O(a + b), Hence, the time complexity is still O(n)

Time complexity of Intersect:
linkedlist a has O(a) 
linkedlist b has O(b)
Therefore, the intersect is O(a N b). As it ignores list items that don't match, the time complexity is O(n) being a linkedlist. 

Overall, the time complexity is Linear O(n). This means the algorithm increases or decreases with the number of inputs.

Space Complexity Analysis:

Space complexity of Union:
linkedlist a has O(a) a being the number of input data in the first linkedlist 
linkedlist b has O(b) b being the number of input data in the second linkedlist
Therefore, the union is O(a + b), Hence, the time complexity is O(n)

Space complexity of Intersect:
linkedlist a has O(a) 
linkedlist b has O(b)
Therefore, the intersect is O(a N b) = O(n). As it ignores list items that don't match, the space complexity is O(n) being a linkedlist of the unique input data (n).

Overall the space complexity is linear, O(n). The more the input elements of each linkedlist, the more the value of the union or intersect generated from it.