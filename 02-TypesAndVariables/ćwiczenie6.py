word = 'X-DSPAM-Confidence: 0.8475'
index = word.find(' ')
print(index)
ostatni = word.find('5', index)
print(ostatni)
host = float(word[index+1:ostatni+1])
print(host)