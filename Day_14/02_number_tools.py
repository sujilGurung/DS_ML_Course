def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(base, n):
    if n == 0:
        return 1
    return base * power(base, n - 1)


def count_vowels(word):
    if word == "":
        return 0
    if word[0].lower() in "aeiou":
        return 1 + count_vowels(word[1:])
    return count_vowels(word[1:])


print("5! =", factorial(5))
print("Digits of 4567 add to", sum_digits(4567))

print("Fibonacci:", end=" ")
for i in range(8):
    print(fibonacci(i), end=" ")
print()

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a power: "))
print(f"{num1} to the power {num2} is: {power(num1, num2)}")

word = input("Enter a word: ")
print(f"Vowels in {word}: {count_vowels(word)}")