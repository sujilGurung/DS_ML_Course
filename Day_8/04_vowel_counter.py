text = input("Type a sentence: ").lower()
vowels = 0
space = text.count(" ")
back =""
for letter in text[::-1]:
    if letter in "aeiou":
        vowels += 1
        back += letter 
        print(letter)
        

print(f"Spaces are {space}")
print(f"Vowels: {vowels}")
print(f"Backwards: {back}")
# print(back)

# Type a sentence: I love Nepal
# Vowels: 5

# Your job:
# 1. also count the spaces
# 2. print the sentence backwards with a loop
#    (hint: start with back = "", then back = letter + back)