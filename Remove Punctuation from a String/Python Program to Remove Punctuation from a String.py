#By Daliah Aljutayli
#Python Program to Remove Punctuation from a String
#-----------------------------------------------

#define punctuation
punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''


string = input('Write a String: ')

#Remove punctuation
NoPun =''

for c in string: #c iterate inside the string
    if c not in punctuation: # check if c not equal any of punctuation symbols!
        NoPun = NoPun + c 

print(NoPun) # After removing punctuation


