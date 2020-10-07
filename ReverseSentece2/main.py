def find_spaces(sentence):
  words_arr = []
  i, j = 0, 0
  while j < len(sentence):
    while sentence[j] == ' ' and j < len(sentence)-1:
      j+=1
      i = j
    while sentence[j] != ' ' and j < len(sentence)-1:
      j+=1
    if j == len(sentence)-1 and sentence[j] != ' ':
      j+=1

    if i != j:
      word = [i,j-1]
      words_arr.append(word)
    else:
      j+=1
  return words_arr

def create_words(words_arr,arr):
  words = []
  for i in range(len(words_arr)):
    limits = words_arr[len(words_arr)-1-i]
    start = limits[0]
    end = limits[1]+1
    words.append(''.join(arr[start:end]))
  return words

def pretty_print(words):
  print(" ".join(words))

sentence = "  hello my fasdfasdf    sadfasdfa   riend is juan and a friend    "
arr = list(sentence)
words_arr = find_spaces(arr)
words = create_words(words_arr,arr)
pretty_print(words)