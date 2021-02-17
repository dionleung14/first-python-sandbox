def greet_user(first_name, last_name):
  print(f'Ayeeee whaddup, {first_name} {last_name}')
  print('Welcome aboard')


print('Start')
greet_user('Leung', last_name='Dion')
# Leung is a positional argument
# Dion is a keyword argument
# Keyword args must come after positional args
print('Finish')

name = input('What is your name?')

def print_user(user):
  print(f'Ayeeee whaddup, {user}')


print_user(name)

def square(number):
  return number * number

# ans = square(int(input('Give me a number: ')))
print(f'Your new number is {square(53)}')
# print(f'Your new number is {ans}')