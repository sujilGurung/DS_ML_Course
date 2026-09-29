s1 = input("Sentence 1: ").lower()
s2 = input("Sentence 2: ").lower()

words1 = set(s1.split())
words2 = set(s2.split())

common = words1 & words2
print("Common words:", sorted(common))

# 1. all_words = words1 | words2, print it sorted
all_words = words1 | words2
print("All words:", sorted(all_words))

# 2. counts = (len(common), len(all_words))
counts = (len(common), len(all_words))

# 3. unpack counts into two names and print them
common_count, total_count = counts
print("Common count:", common_count)
print("Total count:", total_count)

# 4. words in only one sentence (^)
only_one = words1 ^ words2
print("Only in one sentence:", sorted(only_one))