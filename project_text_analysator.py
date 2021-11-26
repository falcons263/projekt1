# definice proměnných
registred_users = {"bob": "123", "ann":"pass123","mike":"password123","liz":"pass123"}
sep = '-' * 50

# požádámě o jméno a heslo
username = input("Write your username: ")
pswd = input("Write password: ")

# ověříme správnost jména a hesla
if pswd == registred_users.get(username):
  print('username:', username)
  print('password:', pswd)
else:
    print('Wrong password or name')
print(sep)

'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# pozdrav uživateli

print('Welcome to the app,', username,'.')
print('We have 3 texts to be analysed.')
print(sep)
while True:
  text = input(str('Enter number between 1 and 3 to select: '))
  # podminka pro overeni spravne zadane hodnoty
  if text.isnumeric() == False or int(text) not in range(1,4):
    print('Wrong value')
  else:
    break
print(sep)

# ověření vybraného textu
#print(TEXTS[int(text) - 1])

# odstranění nepotřebných znaků a oddělení slov
clean_words = [word.strip("@{}&~ˇ^˘°˛`„´˝÷<>*,.()#đ“\n") for word in TEXTS[int(text)-1].split() if word != word.isalpha()]
#clean_words = [word.strip(",.()") for word in TEXTS[int(text)-1].split()]
#print(clean_words)

# zjistíme celkový počet slov
print('There are', len(clean_words), 'words in the selected text.')

# najdeme slova psaná velkými písmeny
#for i in clean_words:
    #if i.isupper():
        #print(i)

# počet slov s velkým počátečním písmenem
num_title = 0
for i in clean_words:
  if i.istitle() == True:
    num_title += 1
print('There are', num_title, 'titlecase words.')

# počet slov psaných velkými písmeny
num_upper = 0
for i in clean_words:
  if i.isupper() == True:
    # odstranění slov obsahující číslice_resp.podminka, ze slovo obsahuje jen pismena
    if i.isalpha() == True:
      num_upper +=  1
print('There are', num_upper, 'uppercase words.')

# počet slov psaných malými písmeny
num_lower = 0
for i in clean_words:
  if i.islower() == True:
    num_lower += 1
print('There are', num_lower, 'lowercase words.')

# počet čísel
num_numeric = 0
for i in clean_words:
  if i.isnumeric() == True:
    num_numeric += 1
print('There are', num_numeric, 'numeric words.')

# součet všech čísel
sum_numbers = 0
for i in clean_words:
  if i.isnumeric() == True:
    sum_numbers += int(i)
print('The sum of all the numbers is', sum_numbers,'.')

print(sep)

# vypíšeme ke každému slovu počet písmen
word_len = {}
for word in clean_words:
    word_len[word] = len(word)

#word_len

# vytvoříme list hodnot
values_list = word_len.values()
#values_list

# najdeme hodnotu nejvyššího počtu písmen ve slově
max_value = max(word_len.values())
#print(max_value)

# vytvoření proměnných pro tabulku/graf
gap_1 = ' '
gap_2 = ' ' * 2
gap = ' ' * (15 - len('OCCUREANCE'))

print(sep)
print(f'LEN|OCCURENCES{gap}|NR.')
print(sep)

# smyčka, která zjistí a vytiskne počet výskytů dle počtu písmen ve slovech
for i in range(1, max_value + 1):
    # for i in range(1,12):

    i_num = list(word_len.values()).count(i)

    chart = '*' * i_num
    width = ' ' * (15 - int(i_num))
    # gap_1 = ' '
    # gap_2 = ' ' * 2

    if i < 10:
        print(f'{i}{gap_2}|{chart}{width}|{i_num}')

    else:
        print(f'{i}{gap_1}|{chart}{width}|{i_num}')






