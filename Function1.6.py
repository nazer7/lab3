import itertools
import math
def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])
sentence = (input("Введите s: "))
print(reverse_sentence(sentence))