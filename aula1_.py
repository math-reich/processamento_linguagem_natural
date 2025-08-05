# matheus, this  hehe

class WordData:
  def __init__(self, original_word, ngrams):
    self.base_word = original_word
    self.pairs = ['abacate', 'abacaxi', 'abobora', 'abobrinha', 
                  'ananás', 'maça', 'mamão', 'manga', 'melancia', 
                  'melão', 'mexerica', 'morango']
    self.ngrams = ngrams

def compare_words(base, word, ngram = 2):
  words = [base, word]
  for w in words:
    for gram in w:
      print("oi")

base_of_words = 
separated_words = []
ngrams = 2

# function to separate array of words
for word in base_of_words:
    separ_word = []
    for index, char in enumerate(word):
      if(index + 1 < len(word)):
         separ_word.append(word[index] + word[index + 1])
    separated_words.append(separ_word)

# function to print array of words
print(list(separated_words))

# function to calculate the distance
# grams em comum * 2  / (grams unicos pal1 + grams unicos pal2)

# need to handle utf8 or ASCII