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