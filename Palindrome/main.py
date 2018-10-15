# Palindrome
# By Matt Halliday

# Variable
word = ""

vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")


countVowels = 0
countConsonants = 0

# Asking user to input the word
while word == "":
    word=input("Please enter the word: ")

# Storage variables
word = word.replace(" ", "")
word = word.casefold()
rev_word = reversed(word)


# Counting vowls and const
for items in word:
    if items in vowels:
        countVowels = countVowels+1
    if items in consonants:
        countConsonants = countConsonants+1

        
# Directory scanning




# Writing to file
if list(word) == list(rev_word):
    file = open("palindrome.txt", "a")
    file.write(word + "\n")
    file.close()
    print("File: has been written.")
    print(countVowels, " vowels")
    print(countConsonants, " consonants")
else:
    print("It is not a palindrome")
    print(countVowels, " vowels")
    print(countConsonants, " consonants")

