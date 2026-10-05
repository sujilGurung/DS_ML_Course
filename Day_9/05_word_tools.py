
def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def count_spaces(text):
    return text.count(" ")
def first_letters(text):
    words = text.split()
    firsts = ""
    for word in words:
        firsts += word[0]
    return firsts

print(count_vowels("I love Nepal"))   
print(is_palindrome("Madam"))         
print(is_palindrome("Nepal"))         
print(count_spaces("I love Nepal"))   
print(first_letters("I love Nepal"))  
