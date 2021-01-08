#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

def utility(filename):
  """Returns a word/count dict for this filename."""
 
  word_count = {} 
  input_file = open(filename, 'r')
  for line in input_file:
    # print (line)
    words = line.split()
    # print(words)
    for word in words:
      word = word.lower()
      
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  input_file.close() 
  # print(word_count)
  return word_count


def print_words(filename):
  
  word_count = utility(filename)
  words = sorted(word_count.keys())
  # print(words)
  for word in words:
    print('number of repeated words in file')
    print (word, word_count[word])




def print_top(filename):
  
  word_count = utility(filename)

 
  items = sorted(word_count.items(), key=lambda x :x[1], reverse=True)
  # print(items)
 
  for item in items[:20]:
    print('the first 20 words with highest repeated number of counts')
    print (item[0], item[1])


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print(sys.argv)
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(0)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(0)
  
if __name__ == '__main__':
  main()
