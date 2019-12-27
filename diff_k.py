"""
Example:
    Given an array of distinct integer values, count the number of pairs of integers that have
    given difference k. For example, given the array {1, 7, 5, 9, 2, 12, 3} and the difference
    k = 2, there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9).
"""


def diff_k(arr=[], k=2):

    dictionary = {}
    index = 0
    for val in arr:
        dictionary[val] = index
        index += 1
    checked = {}   # empty dictionary for values whether they are processed or not
    for val in arr:
        checked[val] = False

    for val in dictionary:
        if val - k in dictionary and checked[val-k] is False:
            print(val, ",", val - k)
        if val + k in dictionary and checked[val+k] is False:
            print(val, ",", val + k)
        checked[val] = True


arr = [1, 7, 5, 9, 2, 12, 3]
k = 2
diff_k(arr, k)

