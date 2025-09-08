def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()

  return file_contents

def count_words(book_text):
  number_of_words = len(book_text.split())
  
  return number_of_words

def main():
  book_contents = get_book_text("./books/frankenstein.txt")
  
  num_words = count_words(book_contents)

  print(f"{num_words} words found in the document")

main()