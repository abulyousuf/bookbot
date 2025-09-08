def get_num_words(book_text):
  number_of_words = len(book_text.split())
  
  return number_of_words

def get_num_chars(book_text):
  freq = {}

  for char in book_text.lower():
    if char == " ":
      continue

    if char == "\n":
      continue

    if char in freq:
      freq[char] += 1
    else:
      freq[char] = 1

  return freq

def sort_on(items):
  return items["num"]

def get_sorted_list(num_chars_dict):
  key_value_dict = [
    {"char": c, "num": n}
    for c, n in num_chars_dict.items()
  ]

  key_value_dict.sort(reverse=True, key=sort_on)
  return key_value_dict