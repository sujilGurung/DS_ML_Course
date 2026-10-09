marks = [67, 45, 92, 78]
def stats(*numbers):
    if len(numbers) == 0:
        return None
    average = round(sum(numbers) / len(numbers), 2)
    return min(numbers), max(numbers), average, len(numbers)

low, high, avg, count = stats(12, 45, 7, 30)
print(f"Low: {low}, High: {high}, Average: {avg}, Count: {count}")
# Low: 7, High: 45, Average: 23.5

low, high, avg, count = (stats(*marks))     
print(f"Low: {low}, High: {high}, Average: {avg}, Count: {count}")

