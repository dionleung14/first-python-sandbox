numbers = [1, 2, 3, 4, 2, 1, 10, 5]

# for index in range(len(numbers) + 1):
#   num = numbers[index]
#   if numbers[index + 1] > num:
#     num = numbers[index + 1]

# print(num)

num = numbers[0]
for number in numbers:
  if number > num:
    num = number  
print(num)