from PyDictionary import PyDictionary
word = input('Word?<user inputs a word>:\t')
try:
    myDict = PyDictionary(word)
    print(myDict.getMeanings())
except:
    print(word,'Not found')