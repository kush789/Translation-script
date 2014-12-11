from translate import translatetext
from validate import takelanguages

fromlang,tolang = takelanguages()
text = raw_input("\nEnter text to translate : ")
print translatetext(fromlang,tolang,text)