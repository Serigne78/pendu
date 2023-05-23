mport random
import sys

                                                            

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


my_list = ["python",
    "programme",
    "ordinateur",
    "jeu",
    "musique",
    "livre",
    "cinema",
    "voyage",
    "restaurant",
    "football",
    "basketball",
    "tennis",
    "plage",
    "montagne",
    "chocolat",
    "cafe",
    "pizza",
    "hamburger",
    "glace",
    "gateau",
    "orange",
    "pomme",
    "banane",
    "fraise",
    "ananas",
    "kiwi"]
words = my_list[(random.randint(0, len(my_list) -1))]
list_words= []

for i in range(len(words)):
  list_words.append("_")
print(list_words)

lives =6

while words != list_words:
  find_words = input("Veuillez chosir une lettre: ").lower()
  
  words = list(words)
  
  index =0
  found = False
  
 
  for word in words:
    if words[index] == find_words:
      list_words[index] = find_words
      found = True
    index+=1
  if not found:
    print(stages[lives])
    print("tu t'es trompé réessaye encore")
    lives-=1
  if lives < 0:
    print("You loose")
    print("le mot à trouver est "+ ''.join(words))
    sys.exit()
  
  print(list_words)
print("You win")
  

    
    

  

 



