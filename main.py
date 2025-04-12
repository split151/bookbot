from stats import count_strings, count_char, sorted_count
import sys

if len(sys.argv) < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1) # Exit with code 1 to stop the code because the program was not run with the correct argument

book_path = sys.argv[1] # Our bookpath is going to be the second argument of sys.argv



def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents
  
def main(path):
  book_contents = (get_book_text(path))
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}")
  print("----------- Word Count ----------")
  count_strings(path)
  print("--------- Character Count -------")
  counted_chars = count_char(path)
  #print(counted_chars)
  sorted_count(counted_chars)
  print("============= END ===============")

main(book_path)