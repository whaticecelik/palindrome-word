word = str(input("enter a word to see if its polindrome or not: "))
reversed_word = word[::-1]
#word_backwords = ''.join(reversed(word_forwards))

if word == reversed_word:
  print(word + " is a polindrome word. Because it can be read the same forwards and backwards")
else:
  print(word + " is not a polindrome word. The reverse of "+ word+ " is "+ reversed_word)
