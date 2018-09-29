# Calculates the total possible permutations given the
# number of characters


def calcPerms(size):
    permutations = 1
    for i in range(2, size + 1):
        permutations = i * permutations
    return permutations

# Recursively calculates the total possible permutations given
# the number of characters


def calcPermsRecursive(n):
    if n > 1:
        return calcPermsRecursive(n - 1) * n
    else:
        return 1

# Get the nth permutation of the input character array, where
# permutation 1 is the same as the input.


def getNthPermutation(chars, n):
    permutations = calcPerms(len(chars))
    x = permutations // len(chars)
    nthPermutation = []

    while len(chars) > 1:
        if n % x != 0:
            nthPermutation.append(chars.pop(n // x))
            n = n % x
        else:
            nthPermutation.append(chars.pop(n // x - 1))
            n = n // (n // x)
        permutations = x
        x = permutations // len(chars)

    nthPermutation.append(chars.pop(0))
    return nthPermutation


# Get the nth permutation of the input character array assuming
# permutation 1 is the input sorted.


def getPermutationNumber(chars):
    sortedCharArray = chars[:]  # deep copy the array
    sortedCharArray.sort()
    permutations = calcPerms(len(sortedCharArray))
    x = permutations // len(sortedCharArray)
    nthPermutation = 0

    for i in range(0, len(chars) - 1):
        nthPermutation += x * sortedCharArray.index(chars[i])
        sortedCharArray.pop(sortedCharArray.index(chars[i]))
        permutations = x
        x = permutations // len(sortedCharArray)
    nthPermutation += 1

    return nthPermutation
