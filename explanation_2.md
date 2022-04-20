This is used to find files within the operating system (os). This involves the use of the "import os" to enable us to be able to traverse a folder down to the file we are looking for.
A recursive data structure is used because the nature of finding files requires traversing the folders down to the required file.

Time Complexity Analysis:

If T is 0 in the case where suffix == "", we return 0, Hence, T is O(1)
If T is greater than 0, T > 0 where, the suffix is a valid value and not an empty list or string:
we return T(n) where n is the number of subfolders in the main folder
In this case T(n) = T(n) + c. That is the higher the number of sub folders in main folder, the longer it will take to traverse the folders. Hence, the time complexity is O(n) where "n" refers to the number of subfolders in the main folder

Space Complexity Analysis:

The maximum depth is 5 as there are 5 sub-folders in the main folder that would be traversed to find the file. The maximum depth is "n".
The space is directly proportionate to "n". Hence, the deeper the sub folders the more space that would be required to run the recursive function. Hence, it has a linear relationship or time complexity of O(n).
