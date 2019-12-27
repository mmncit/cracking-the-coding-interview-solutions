"""
Example:
    Print all the positive integer solutions to the equation a^3 + b^3 = c^3 + d^3 where
    a, b, c, d are integers between 1 and n
"""

def cubic_sum(n):
    dictionary = {}
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dictionary[pow(a, 3) + pow(b, 3)] = [a, b]

    for c in range(1, n + 1):
        for d in range(1, n + 1):
            if pow(c, 3) + pow(d, 3) in dictionary:
                [a, b] = dictionary[pow(c, 3) + pow(d, 3)]
                print(a, b, c, d, "|", pow(c, 3) + pow(d, 3))

cubic_sum(1000)