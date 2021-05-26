from itertools import permutations

from dynamic.stringInterleaving import isInterleave


def allInterleave(str1, str2):
    totalPermutation = []
    for i in permutations(str1 + str2):
        temp = ''.join(i)
        if isInterleave(str1, str2, temp):
            totalPermutation.append(temp)
    return totalPermutation


if __name__ == '__main__':
    result = allInterleave('ab', 'yz')
    print("Total Combinations is : " + str(len(result)))
    for item in result:
        print(item)
