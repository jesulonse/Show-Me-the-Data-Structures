Active directory consists of group(s) and user(s). Some groups contain(superset of) other groups while the users are subset of the groups.
A recursive data structure is used because it is used to traverse the groups down to the user to determine if a group is a subset of another group or a user is a subset of a group.

Time Complexity Analysis:

The base case when the user is not in the group, then it returns False. That way, the time complexity, T(n) is O(1).
If the user is found in the group, then it return True, T(n)
If the group is subset of another group, T(n) = T(n) + c 
Since c is a constant, T(n) = T(n). Therefore, the more the traverse (n) through the parent group down to the user, the more the time T(n) it takes to run the recursive function. Hence, the time complexity is O(n).


Space Complexity Analysis:

The maximum depth is 3 as we added a child group to the parent group and the child group itself has its subset of sub child. The maximum depth is "n" being as a result of the number of subset group (down to the the user in the group) in the groups.
The space is directly proportionate to "n". Hence, the deeper the sub folders the more space that would be required to run the recursive function. Hence, it has a linear relationship or time complexity of O(n).