x = int(input())
sum_of_numbers = 0
while x:
    sum_of_numbers += x % 10
    x //= 10
print(sum_of_numbers)
