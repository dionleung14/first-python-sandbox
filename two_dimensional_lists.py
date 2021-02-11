matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
# print(matrix[0][2])

# for row in matrix:
#   for item in row:
#     print(item)


numbers = [5, 2, 1, 5, 7, 4, 5]
# numbers.append('hey')
# numbers.insert(1, 4)
# numbers.remove(5)
# del numbers[5]
# print(numbers.count(5))
# print(numbers.pop())
# print(numbers)
# print(numbers.index(7))
# print(1 in numbers)
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# print(numbers)

print(numbers)
for number in numbers:
  while numbers.count(number) > 1:
    numbers.remove(number)
    # print(f"Current number is {number}. There are {numbers.count(number)} in the list")
print(numbers) # keeps the non duplicate at the end...

answer_numbers = [2, 2, 4, 6, 2, 4, 6, 1]
uniques = []
for number in answer_numbers:
  if number not in uniques:
    uniques.append(number)
print (uniques)