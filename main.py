highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(",")

highlighted_poems_stripped = []
for item in highlighted_poems_list:
  strippi = item.strip()
  highlighted_poems_stripped.append(strippi)



highlighted_poems_details = []
for item in highlighted_poems_stripped:
  highlighted_poems_details.append(item.split(":"))



titles = []
poets = []
dates = []

for item in highlighted_poems_details:
  titles.append(item[0])
  poets.append(item[1])
  dates.append(item[2])

for item in poets:
  teksti ="The poem {TITLE} was published by {POET} in {DATE}."
  teksti.format(TITLE = titles, POET = poets, DATE = dates)

jotain = "liibalaaba"

when_you_are_old = \
  """When you are old and grey and full of sleep,
  And nodding by the fire, take down this book,
  And slowly read, and dream of the soft look
  Your eyes had once, and of their shadows deep;
  
  How many loved your moments of glad grace,
  And loved your beauty with love false or true,
  But one man loved the pilgrim soul in you,
  And loved the sorrows of your changing face;
  
  And bending down beside the glowing bars,
  Murmur, a little sadly, how Love fled
  And paced upon the mountains overhead
  And hid his face amid a crowd of stars."""


list_of_lines = when_you_are_old.split("\n")

print(list_of_lines)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

# Uncomment these function calls to test your function:
#print(unique_english_letters("mississippi"))
# should print 4
#print(unique_english_letters("Apple"))
# should print 4