def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print(f"Armstrong numbers between {start} and {end} are:")
for number in range(start, end + 1):
    if is_armstrong(number):
        print(number)
