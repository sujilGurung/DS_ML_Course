count = 0
for n in range(1, 51):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
        count += 1
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

print(f"Fizz: {count}")

# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz

# Your job:
# 1. go up to 50
# 2. count how many times Fizz was printed
