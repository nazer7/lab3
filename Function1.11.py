def is_palindrome(text):
    text = text.replace(" ", "").lower()  
    return text == text[::-1]  
word = input("enter word or sentence: ")
if is_palindrome(word):
    print("it is palindrome!")
else:
    print("it is not palindrome.")
