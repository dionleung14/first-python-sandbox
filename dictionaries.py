customer = {
  "name": "Dion Leung",
  "age": 26,
  # "age": 36, # Unique keys lol
  "is_verified": True
}

# print(customer.get("birthdate")) # None
# print(customer["birthdate"]) # KeyError

num_to_text = {
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four",
  "5": "Five",
  "6": "Six",
  "7": "Seven",
  "8": "Eight",
  "9": "Nine",
  "0": "Zero"
}

ph_number = input("Phone: ")

word_phone = ""
for digit in ph_number:
  # word_phone += f"{num_to_text[digit]} "
  word_phone += f"{num_to_text.get(digit, '!')} "
  # word_phone += num_to_text.get(digit, "!") +  " "

print(word_phone)

