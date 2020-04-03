# Calculates the total possible permutations given the
# number of characters.  This is the iterative approach to
# calculating factorials.

def calcPerms(size):
    permutations = 1
    for i in range(2, size + 1):
        permutations = i * permutations
    return permutations


# Recursively calculates the total possible permutations given
# the number of characters.  This is the definition of a factorial.

def calcPermsRecursive(n):
    if n > 1:
        return calcPermsRecursive(n - 1) * n
    else:
        return 1


# Get the nth permutation of the input character array, where
# permutation 1 is the input character array sorted in ascending order.
# -- a set is the number of permutatations where index 0 is constant
#    (ex. [0,1,2] and [0,2,1] are a set)

def getNthPermutation(chars, nthPerm):
    chars.sort()

    if (nthPerm == 0):
        return []

    permutations = calcPerms(len(chars))
    setSize = permutations // len(chars)
    result = []

    while len(chars) > 1:
        if nthPerm % setSize != 0:
            result.append(chars.pop(nthPerm // setSize))
            nthPerm = nthPerm % setSize
        else:
            result.append(chars.pop(nthPerm // setSize - 1))
            nthPerm = nthPerm // (nthPerm // setSize)
        permutations = setSize
        setSize = permutations // len(chars)

    result.append(chars.pop(0))
    return result


# Get the permutation number of the input character array assuming
# permutation 1 is the input sorted.

def getPermutationNumber(chars):
    sortedCharArray = chars[:]  # deep copy the array
    sortedCharArray.sort()
    permutations = calcPerms(len(sortedCharArray))
    setSize = permutations // len(sortedCharArray)
    nthPermutation = 0

    for i in range(0, len(chars) - 1):
        nthPermutation += setSize * sortedCharArray.index(chars[i])
        sortedCharArray.pop(sortedCharArray.index(chars[i]))
        permutations = setSize
        setSize = permutations // len(sortedCharArray)
    nthPermutation += 1

    return nthPermutation
