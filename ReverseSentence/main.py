def reverse_words(sentence, length):
  i = 0
  j = 0
  while(i< length):
    while(i<j or i < length and sentence[i] == ' '):
      i=i+1
    while(j < i or j < length and sentence[j] != ' '):
      j=j+1
    reverse(sentence, i, j-1)

def clean_spaces(sentence, length):
  i = 0
  j = 0
  while(j<length):
    while(j < length and sentence[j] == ' '):
      j+=1
    while(j < length and sentence[j] != ' '):
      i+=1
      j+=1
      sentence[i] = sentence[j]
    while(j < length and sentence[j] == ' '):
      j+=1
    if (j < length):
      i+=1
      sentence[i] = ' '
  print(sentence)

def reverse(sentence, i, j):
  while(i<j):
    last = sentence[j]
    first = sentence[i]
    sentence[i]=last
    sentence[j]=first
    i+=1
    j-=1     
  print(sentence)

sentence = "hello    my friend "
length = len(sentence)
ls = list(sentence)
reverse(ls, 0, length-1)
reverse_words(ls, length)
# clean_spaces(sentence,length)
# reverse(ls, 0, length-1)