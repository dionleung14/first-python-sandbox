# for item in "Test":
#   print(item)
#   # prints T, e, s, t

# for item in ['yes', 'no', 'maybe so']:
#   print(item)
#   # prints yes, no, maybe so

# for item in range(10):
#   print(item)
#   # prints 0, 1, 2, ..., 8, 9

# for item in range(5, 10):
#   print(item)
#   # prints 5, 6, 7, 8, 9

# for item in range(5, 10, 2): # start is 5, end is 10, step is 2
#   print(item)
#   # prints 5, 7, 9

prices = [10, 20, 30]
total = 0
for cost in prices:
  total += cost
print(f"Your total is {total}")