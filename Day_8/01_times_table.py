num = int(input("Which table? "))
upto = int(input("Up. to?"))
answer = 0
for i in range(1, upto + 1):
    print(f"{num} x {i} = {num * i}")
    
    answer += num * i
print(f"The total of {num} table up to {upto} is {answer}")
    

