
#* Asked in Facebook

#? Given a sentence, reverse each word in the string.

#! Example:
#? Input: What is your name?
#? Output: tahW si ruoy ?eman

def rev_words(sen):
  ls = sen.split()
  
  for i in range(len(ls)):
    ls[i] = ls[i][::-1]
  
  sen = ""
  for i in ls:
    sen += i
    sen += " "
  
  return sen.rstrip()

sentence = "What is your name?"
print(rev_words(sentence))
#tahW si ruoy ?eman 