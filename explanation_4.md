Active directory consists of group(s) and user(s). Some groups contain(superset of) other groups while the users are subset of the groups.
A recursive data structure is used because it is used to traverse the groups down to the user to determine if a group is a subset of another group or a user is a subset of a group
The time complexity is Linear O(n) because of the Single for loop in the "walk_through(present_group)" function. This means the algorithm increases or decreases with the number of inputs.