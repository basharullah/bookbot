from stats import get_num_words, get_num_chars, sort_dict_by_value
import sys



def get_book_text(book_path):
  with open(book_path) as f:
    file_contents = f.read()
  return file_contents


def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_text = get_book_text(sys.argv[1])
  no_of_words = get_num_words(book_text)
  ssorted = sort_dict_by_value(get_num_chars(book_text))
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  print(f"Found {no_of_words} total words")
  print("--------- Character Count -------")
  for i in ssorted:
    if i["char"].isalpha():
      print(f"{i["char"]}: {i["num"]}")

main()