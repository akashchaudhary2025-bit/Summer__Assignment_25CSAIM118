def is_perfect(num):
    if num < 1:
        return False

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    return divisors_sum == num

number = int(input("Enter a number: "))

if is_perfect(number):
    print(f"{number} is a Perfect Number.")
else:
    print(f"{number} is not a Perfect Number.")
