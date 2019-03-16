#/usr/bin/python
import nltk
from nltk.corpus import wordnet

from itertools import permutations
perms = [''.join(p) for p in permutations('Protosem')]

for i in perms :
    if not wordnet.synsets(i):
        pass
    else:
        print (i)
   