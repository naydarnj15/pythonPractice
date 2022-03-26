count = 0
average = 0
total = 0

num = input("Enter a number: ")

while(num != "done"):
    count += 1
    total += int(num)
    average = total / count
    num = input("Enter a number: ")

