def get_num_words(book_text):
  number_of_words = len(book_text.split())
  
  return number_of_words

def get_num_chars(book_text):
  freq = {}

  for char in book_text.lower():
    if char == " ":
      if char in freq:
        freq[char] += 1
      else:
        freq[char] = 1

    if char in freq:
      freq[char] += 1
    else:
      freq[char] = 1
      
  return freq