# for x in range(4):
#   for y in range(3):
#     print(f'({x}), ({y})')


# numbers = [5, 2, 5, 2, 2] # prints an F
numbers = [2, 2, 2, 2, 6] # prints an L
character = 'x'

# for number in numbers:
#   print(character * number)
#   # works lol

# nested loop solution:
for number in numbers:
  string = ""
  for count in range(number):
    string += "x"
  print(string)