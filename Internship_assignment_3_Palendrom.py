def is_palindrome(word):
    # word = word.lower
    word_reverse = word[::-1]
    if word == word_reverse:
        return True
    return False
user_word = input("Enter a single word: ")
w = user_word.lower()
if is_palindrome(w):
    print(f"The {user_word} is a palindrome.")
else:
    print(f"The {user_word} is not a palindrome.")
