sentence = input("Enter a sentence: ").title()
words = sentence.split()
if sentence == "":
    print("Enter a sentence its empty")
else:
    print(sorted(words, key=len))
    print(max(words, key=len))
    print(list(filter(lambda w: len(w) > 3, words)))
    print(list(map(lambda w: w.capitalize(), words)))
    print(" ".join(map(lambda w: w[::-1].capitalize(), words)))
    print(len(list(filter(lambda x: x[0] in "AEIOU", words))))

# ['a', 'is', 'to', 'fun', 'very', 'learn', 'python', 'language']
# language
# ['python', 'very', 'language', 'learn']
# ['Python', 'Is', 'A', 'Very', 'Fun', 'Language', 'To', 'Learn']
# nohtyp si a yrev nuf egaugnal ot nrael

# Your job:
# 1. count the words that start with a vowel
#    (hint: filter + w[0] in "aeiou" + len)
# 2. get the sentence from the user with input()