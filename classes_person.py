class Person:
  def __init__(self, name):
    self.name = name
  
  def talk(self):
    print(f'Hello there, I am {self.name}')


jess = Person('Jess')
jess.talk()
print(jess.name)