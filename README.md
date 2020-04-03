# Background
This project came from solving project euler problem [24](https://projecteuler.net/problem=24).  I had so much fun coming up with this algorithm that I took it even further by building more functions around computing permutations and writing these docs.

# Calculating the total possible permutations
Calculating the total permutatations for an array of characters is defined by the factorial equation, where *n* is the size of the input array.
```
n! = n(n-1)(n-2)...(2)(1)
```
This library contains two functions for calculating the number of permutations.  One is recursive, as it is the definition of a factorial, but it has a space limitation for how large *n* can be.  The other is iterative for better performance.  Both functions take the same input and produce the same output.

# Getting the *nth* permutation of a character array
To get the nth permutation of an array of characters, use the following code example, where **chars** is an array of characters, and **nthPerm** is an integer representing the nth permutation of the character array, assuming permutation one is character array sorted in ascending alphanumeric order.
```python
chars = ['0','1','2']
nthPerm = 3
print(getNthPermutation(chars, nthPerm))
# console: ['1','0','2']
```
This algorithm provides quick lookup for permutations, being very efficient with a time complexity of O(n).  This is important because permutations grow rapidly as the array size increases.  An input character array with 15 elements has over 1 trillion permutations, but this algorithm only needs 15 iterations to find any of the 1 trillion permutations.

### How it works
Let's say we have an array of characters with the values ['0','1','2'].  This array has six possible permutations, and they are:
```
1. ['0','1','2']
2. ['0','2','1']
3. ['1','0','2']
4. ['1','2','0']
5. ['2','0','1']
6. ['2','1','0']
```
Let's say we wish to find the 3rd permutation of the array using the getNthPermutation(chars, nthPerm) function.  

First, the function would find the starting set size for the 6 permutations we currently have.  The set size is the number of permutations that have the same character in the first position of the array.  For the above example, we can clearly see that the set size is two.
```
# Both permutations have '0' in the first position
['0','1','2']
['0','2','1']

# Both permutatations have '1' in the first position
['1','0','2']
['1','2','0']
 
# Both permutations have '2' in the first position
['2','0','1']
['2','1','0']
```
Fortunately, there is a mathematical relationship between # of permutations and the set size.  It is defined as:
```
setSize = permutations // len(chars)  # // is integer division
```
So for the above example, setSize = 6 // 3 = 2.

The function use the set size to determine which set of permutations it will focus on.  If we are trying to find the 3rd permutation then the function will evaluate the following condition:
```
nthPerm % setSize != 0
3 % 2 = 1, 1 != 0
```
If the condition evaluates to anything except 0, it means the permutation it is interested in is not the last permutation in the set.  In this case, the function will pop the character located at:
```
chars[nthPerm // setSize] === chars[3 // 2] === chars[1] = '1'
```
The new character array is now ['1'], and the old character array is now ['0','2'].  Because index 1 was popped from the char array, the new permutations will represent the second set with the first character removed.  The function resets the setSize and permutations accordingly to deal with these new permutations.

Set
```
3. ['1','0','2']
4. ['1','2','0']
```
becomes...
```
1. ['0','2']
2. ['2','0']

nthPerm = nthPerm % setSize === 3 % 2 = 1
permutations = setSize = 2
setSize = permutations // len(chars) === 2 // 2 = 1
```

Again, the function evaluates the condition:
```
nthPerm % setSize != 0
1 % 1 = 0, 0 == 0
```
Since it evaluates to zero, the function now uses a slightly different equation to extract the next character:
```
chars[nthPerm // setSize - 1] === chars[1 // 1 - 1] === chars[0] = '0'
```
so, our new character array is now ['1','0'], and our old character array is now ['2'].  Since there is only one character left, the function just pops the last one and appends it to the new character array.  The final result is ['1','0','2'].

# Getting the permutation number of a character array
To get the permutatation number of a character array, use the following code example, where **chars** is the character array and permutation 1 is the character array sorted in ascending ASCII values.
```python
chars = ['1','0','2']
print(getPermutationNumber(chars))
# console: 3
```
Like the previous algorithm, this one also operates with a time complexity of O(n).

### How it works
Let's say we have an array of characters called **chars** with the values ['1','0','2'].  This array has six possible permutations, and we want to find the permutation number that represents this array.
```
1. ['0','1','2']
2. ['0','2','1']
3. ['1','0','2']
4. ['1','2','0']
5. ['2','0','1']
6. ['2','1','0']
```
The getPermutationNumber(chars) function starts by sorting **chars** in ascending ASCII order.  This sorted array becomes permutation 1.  The function also calculates the total **permutations** and the **setSize**.  **nthPermutation** starts at 0 because we add to it throughout the loop.
```
sortedChars = ['0','1','2']
permutations = 6
setSize = 2
nthPermutation = 0
```
The function loops 3 times because our **chars** array has 3 items.  For each iteration of the loop, the function will add to **nthPermutation** the **setSize** multiplied by the index number in **sortedChars** that contains the first item in the **chars** array.
```
chars = ['1','0','2']
sortedChars = ['0','1','2']
i = 0
nthPermutation += setSize * sortedChars.index(chars[i])
                = 2 * sortedCharArray.index('1')
                = 2 * 1
                = 2
nthPermutation = 2
```
The first iteration of the loop tells us that the nthPermutation of **chars** is at least 2, because the set size is two, and character '1' appears in the second set of permutations as indicated by it's position in **sortedChars**.  To prepare for the second loop, the function removes the character '1' from **sortedChars**. It then recalculates **permutations** and **setSize** and **nthPermutation**.
```
chars = ['1','0','2']
sortedChars = ['0','2']
permutations = 2
setSize = 1
i = 1
nthPermutation += setSize * sortedChars.index(chars[i])
                = 1 * sortedCharArray.index('0')
                = 1 * 0
                = 0
nthPermutation = 2
```
The loop terminates since it is now on the last element and there is no need to calculate further.  Instead, it just adds 1 to nthPermutation, which now equals 3.
