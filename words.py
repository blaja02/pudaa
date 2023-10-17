#def count_words(wordstoinsert, word):
 #   counter = 0
  #  consecutive_count = 0
    
  #  for i in range(wordstoinsert):
   #     random_word = input("Insert a string: ")
    #    words = random_word.split()
        
       # for w in words:
          #  if w == word:
              #  counter += 1
               # consecutive_count += 1
            #else:
              #  consecutive_count = 0
    
    #return f"You inserted the word {word} {counter} times."

def count_words(wordstoinsert, word):
    counter = 0
    counter2 = 0
    
    for i in range(wordstoinsert):
        random_word = input("Insert a string: ")
        
        # Count the occurrences of the word as a substring in the input
        counter += random_word.count(word)
    
    return f"You inserted the word {word} {counter} times."

print(count_words(2, "mango"))

def count_words(wordstoinsert, word):
    counter = 0
    
    for i in range(wordstoinsert):
        random_word = input("Insert a string: ")
        
        # Count the occurrences of the word as a substring in the input
        counter += random_word.count(word)
    
    return f"You inserted the word {word} {counter} times."

print(count_words(2, "mnam"))
