from stats import get_num_words, get_num_chars, get_sorted_list

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()

  return file_contents

def main():
  book_contents = get_book_text("./books/frankenstein.txt")
  
  num_words = get_num_words(book_contents)

  num_chars = get_num_chars(book_contents)

  sorted_list = get_sorted_list(num_chars)

  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count -----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count ---------")
  for i in sorted_list:
    print(f"{i["char"]}: {i["num"]}")

main()