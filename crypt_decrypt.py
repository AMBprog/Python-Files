
import base64
from hashlib import sha256
from getpass import getpass


enter = input("in : ") #Enter the name of your input file
exit = input("out : ") #Enter a name for your output file
key = getpass("key : ") #Give a key

keys = sha256(key.encode('utf-8')).digest()
with open(entree,'rb') as f_entree:
    with open(sortie, 'wb') as f_sortie:
        i = 0
        while f_entree.peek():
            c = ord(f_entree.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            f_sortie.write(b)
            i = i + 1






