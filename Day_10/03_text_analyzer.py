def count_word(report):
    length = len(report.split())
    return length

def unique_words(report):
    return sorted(set(report.lower().split()))

def highest(report):
    return max(report.split(), key=len)

def shortest(report):
    return min(report.split(), key=len)

def count(report):
    counts = {}
    words = report.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

report = input("Enter a sentence: ")

print(f"Letters: {len(report)}")
print(f"Words: {count_word(report)}")
print(f"longest number: {highest(report)}")
print(unique_words(report))
for num, words in enumerate(unique_words(report), start=1):
    print(f"{num}. {words}")
print(count(report))

# Type a sentence: I love momo and I love tea
# Letters: 26
# Words: 7
# Longest word: love
# 1. and
# 2. i
# 3. love
# 4. momo
# 5. tea

# Your job:
# 1. write shortest_word(text) with min()
# 2. count how many times each word appears
#    with a dictionary (Day 06 + Day 08)