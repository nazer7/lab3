import itertools
import math
def string_permutations(s):
    return list(map("".join, itertools.permutations(s)))
s = (input("Введите s: "))
print(string_permutations(s))