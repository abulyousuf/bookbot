from stats import get_num_words, get_num_chars

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()

  return file_contents

def main():
  book_contents = get_book_text("./books/frankenstein.txt")
  
  num_words = get_num_words(book_contents)

  num_chars = get_num_chars(book_contents)

  print(f"{num_words} words found in the document")
  print(num_chars)

main()