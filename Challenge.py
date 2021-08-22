letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  tarkastus = []
  indeks = 0
  for kirjain in word:
    if kirjain in letters and kirjain not in tarkastus:
      indeks+=1
      tarkastus.append(kirjain)
  return indeks

# Uncomment these function calls to test your function:
#print(unique_english_letters("mississippi"))
# should print 4
#print(unique_english_letters("Apple"))
# should print 4
#------------------------------------------------------

# Write your count_char_x function here:
def count_char_x(word, x):
  numero = 0
  for i in word:
    if i == x:
      numero+=1
  return numero

# Uncomment these function calls to test your tip function:
#print(count_char_x("mississippi", "s"))
# should print 4
#print(count_char_x("mississippi", "m"))
# should print 1
#--------------------------------------------------------------

# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  splits = word.split(x)
  return (len(splits)-1)

# Uncomment these function calls to test your function:
#print(count_multi_char_x("apinapa", "ap"))
#-----------------------------------------------------
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  sana = ""
  alku = word.find(start)
  loppu = word.find(end)
  if (alku<loppu and loppu>alku) and (loppu<len(word)):
    sana = word[(alku+1):(loppu)]
    return sana
  else:
    return word
# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"
#---------------------------------------------------
# Write your x_length_words function here:
def x_length_words(sentence, x):
  uusilause = sentence.split()
  vaarin = False
  for sana in uusilause:
    pituus = len(sana)
    if pituus<x:
      vaarin = True
  if vaarin:
    return False
  else:
    return True

# Uncomment these function calls to test your tip function:
#print(x_length_words("i like apples", 2))
# should print False
#print(x_length_words("he likes apples", 2))
# should print True
#--------------------------------------------------------

# Write your check_for_name function here:
def check_for_name(sentence, name):
  nimi = False
  oikeaNimi = name.upper()
  oikeaLause = sentence.upper()
  tsekkaus = oikeaLause.split()
  for x in tsekkaus:
    if x==oikeaNimi:
      nimi = True

  return nimi

  #return true if name in sentence all lowercase or uppercase or mixed
# Uncomment these function calls to test your  function:
#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False
#------------------------------------------------------------

# Write your every_other_letter function here:
def every_other_letter(word):
  indeksi = 0
  lista = ""
  for x in word:
    if indeksi%2==0:
      lista+=(x)
    indeksi +=1
  return lista

# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print

#---------------------------------------------------------------

def reverse_string(word):
  pituus = len(word)
  uusisana = ""
  for i in range(pituus,0,-1):
    uusisana+=word[i-1]
  return uusisana
# Uncomment these function calls to test your  function:
#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print

#----------------------------------------------------------------

# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  a2= word1[0]+word2[1:]
  a1= word2[0]+word1[1:]
  uusisana = a1 + a2
  return uusisana

# Uncomment these function calls to test your function:
#print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
# should print b a

#----------------------------------------------------------------
def add_exclamation(word):
  pituus = len(word)
  if pituus>=20:
    return word
  else:
    indeksi = pituus
    while len(word)<20:
      word+="!"
      indeksi +=1
    return word


# Write your add_exclamation function here:

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
#-------------------------------------------------------------------

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here

updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)

num_records = 0
for item in updated_medical_data:
  if item=="$":
    num_records+=1

print("There are " + str(num_records) + "medical records in the data")