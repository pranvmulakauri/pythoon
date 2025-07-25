# Program for a finding the unique vowels in a given word
def unique_vowel(word1):
    vowels = set("aeiou")
    words1 = word1.lower()
    found = set(words1) & vowels
    return(''.join(found))

# Program counting the number of unique vowels in a given word including duplicates
def no_of_vowels(word):
    words = word.lower()
    vowel = set("aeiou")
    count = 0
    for char in words:
        if char in vowel:
            count += 1
    return count

# Program counting the number of unique vowels in a given word including duplicates
word = input("Enter a word: ")
count_without_duplicates = len(unique_vowel(word))
print(f"The vowels in the given word are: {unique_vowel(word)}")
print(f"The total number of vowels in the word with duplicates: {no_of_vowels(word)}")
print(f"The total number of vowels in the word without duplicates: {count_without_duplicates}")
