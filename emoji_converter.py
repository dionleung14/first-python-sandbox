message = input(">")
emojis = {
  ":)":"😀",
  ":(":"🙁"
}
def emoji_conversion(string):
  words = string.split(' ')
  output = ""
  for word in words:
    output += emojis.get(word, word) + " "
  return output

print(emoji_conversion(message))
# print(words)