# Calculating the total possible permutations
Calculating the total permutatations for an array of characters is defined by the factorial equation, where *n* is the size of the input array.
```
n! = n(n-1)(n-2)...(2)(1)
```
This library contains two functions for calculating the number of permutations.  One is recursive, as it is the definition of a factorial, but it has a space limitation for how large *n* can be.  The other is iterative for better performance.  Both functions take the same input and produce the same output.

# Getting the *nth* permutation of a character array
To get the nth permutation of an array of characters, use the following code example, where **chars** is an array of characters, and **nthPerm** is an integer representing the nth permutation of the character array, assuming permutation 1 is the character array sorted in ascending ASCII values.
```python
chars = ['0','1','2']
nthPerm = 3
print(getNthPermutation(chars, nthPerm))
# console: ['1','0','2']
```
This algorithm provides quick lookup for permutations, being very efficient with a time complexity of O(n).  This is important because permutations grow rapidly as the array size increases.  An input character array with 15 elements has over 1 trillion permutations, but this algorithm only needs 15 iterations to find any of the 1 trillion permutations.

### How it works


# Getting the permutation number of a character array
To get the permutatation number of a character array, use the following code example, where **chars** is the character array and permutation 1 is the character array sorted in ascending ASCII values.
```python
chars = ['1','0','2']
print(getPermutationNumber(chars))
# console: 3
```
Like the previous algorithm, this one also operates with a time complexity of O(n).