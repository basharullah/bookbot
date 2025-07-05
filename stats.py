
def get_num_words(text):
  return len(text.split())

def get_num_chars(text):
  chars_dict = {}
  for char in text.lower():
    if char in chars_dict:
      chars_dict[char] += 1
    else:
      chars_dict[char] = 1
  return chars_dict 



def sort_dict_by_value(d):
  temp_list = []

  for k, v in d.items():
    temp_list.append({"char": k, "num": v})

  temp_list.sort(reverse=True, key=lambda x: x["num"])
  return temp_list