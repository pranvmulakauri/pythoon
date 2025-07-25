#Function for reverse the given string
def revers_string(word):
    return word[::-1]

#Function for reverse internal content of each word
def reverse_word(sentence):
    revers_sentence = sentence.split(' ')[::-1]
    return ' '.join(revers_sentence)

#Function for reverse internal content of each word
def reveres(sen):
    words = sen.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

print("Revers each letter of a word of a string.")
user_word = input("Enter a word as a string:")
print(f"The revers of the given word is '{revers_string(user_word)}'\n")

print("Revers each word of a string")
user_sentence = input("Enter a sentence: ")
print(f"The revers of the given sentence is '{reverse_word(user_sentence)}'\n")

print("Reverse internal content of each word.")
user = input("Enter a sentence:")
print(f"The revers of the given word is '{reveres(user)}'")