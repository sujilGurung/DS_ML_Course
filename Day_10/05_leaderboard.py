
scores = {"Ram": 450, "Sita": 720, "Hari": 380, "Gita": 610}

top = sorted(scores.values(), reverse=True)
print(f"Top 3 scores: {top[:3]}")      # [720, 610, 450]
print(f"Players: {len(scores)}")       # 4
print(f"Total points: {sum(scores.values())}")   # 2160

# key=scores.get: compare the names by their score
print(f"Winner: {max(scores, key=scores.get)}")  # Sita

for num, (name, score) in enumerate(sorted(scores.items()), start=1):
    print(f"{num}. {name} scored {score}")

last = min(scores, key=scores.get)
last_score = scores[last]
print(f"Last scorer is {last} scored {last_score}")
# Your job:
# 1. print every name A to Z, numbered with enumerate()
# 2. print who came last, with min(..., key=scores.get)