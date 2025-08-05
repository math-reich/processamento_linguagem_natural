# matheus, this  hehe

def compare_words(base, word, ngram = 2):
   words = [base, word]
   for w in words:
      for gram in w:
         print("oi")

base_of_words = ['abacate', 'abacaxi', 'abobora', 'abobrinha', 'ananás', 'maça', 'mamão', 'manga', 'melancia', 'melão', 'mexerica', 'morango']
separated_words = []
ngrams = 2

for word in base_of_words:
   for index, char in enumerate(word):
      if(index + 1 < len(word)):
         separated_words.append(word[index] + word[index + 1])

print(list(separated_words))

def teste():
   ## TESTE de logica
   teste = 'abacate'
   teste_separado = []

   # correct way to separate the word
   # like this 'ab' 'ba' 'ac' 'ca' 'at' 'te'
   for index, c in enumerate(teste):
      if(index + 1 < len(teste)):
         teste_separado.append(teste[index] + teste[index + 1])

