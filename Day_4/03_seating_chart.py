chart = [["Empty", "Empty", "Empty", "Empty"],
         ["Empty", "Empty", "Empty", "Empty"],
         ["Empty", "Empty", "Empty", "Empty"]]

name = input("Enter the name: ")
row_num = int(input("Enter row number: "))
column_num = int(input("Enter column number: "))
chart[row_num][column_num] = name

for row in chart:
    print(row)

empty_seats = 0
for rows in chart:
    empty_seats += rows.count("Empty")

print(empty_seats)