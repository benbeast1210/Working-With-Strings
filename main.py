# letter_frequency will take in a word to 
# check, and a letter to check for. It will 
# return an integer denoting the number of 
# times the 'letter' appears in the 'word'.

def letter_frequency():
  word = input()
  letter = input()
  n = len(word)
  
  per = ((word.count(letter)/n)*100)
  
  print(int(per))

# word_length will take in text as input, and
# output an integer denoting the average length
# of eath word in the 'text'.
def word_length():
  text = input()
  
  z = text.split()
  y = len(z)
  x = 0
  
  for i in z:
    x += len(i)
  
  print(x/y)
