def count_strings(filepath):
  with open(filepath) as f:
    num_words = 0
    file_contents = f.read()
    words = file_contents.split()
    for word in words:
      num_words += 1
    print(f"Found {num_words} total words")

def count_char(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    words = file_contents.split()

    char_dict = {}

    for word in words:
      strings = word.split()
      for string in strings:
        for x in string:
          char = x.lower()

          if char in char_dict:
            char_dict[char] += 1
          else:
            char_dict[char] = 1
    return char_dict

def sorted_count(dictionary):
  sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse = True)
  sorted_dict = dict(sorted_items)
  for char, count in sorted_dict.items():
    #print(type(sorted_items))
    if char.isalpha() == True:
      print(f"{char}: {count}")
      
   