# Thanks to https://github.com/ralphleon/Python-Algorithms/blob/master/Cryptology/vigenere.py
# And http://rosettacode.org/wiki/Vigen%C3%A8re_cipher#Python
# Arlefreak

import sys # for command line arguments
import os # to see if a file exists
from itertools import starmap, cycle 

def Decrypt(message, key):

	# single letter decryption.
	def dec(c,k): return chr(((ord(c) - ord(k)) % 26) + ord('A'))
	return "".join(starmap(dec, zip(message, cycle(key))))

def Encrypt(message, key):
	# convert to uppercase.
	# strip out non-alpha characters.
	message = filter(lambda _: _.isalpha(), message.upper())

	# single letter encrpytion.
	def enc(c,k): return chr(((ord(k) + ord(c)) % 26) + ord('A'))
	return "".join(starmap(enc, zip(message, cycle(key)))) 

def Main():

	""" Main function """

	verbose =0
	file = ""
	passkey = ""
	encrypt = 0

	if (len(sys.argv) < 2):
		message = 'usage: vigenere.py [encrypt|decrypt] [-v] [-k key] <file>'
		print(message)
		exit()

	if sys.argv[1] == "encrypt": encrypt = 1
	elif sys.argv[1] == "decrypt": encrypt = 0
	else: 
		message = "unknown option \"",sys.argv[1],"\", must be encrypt or decrypt"
		print (message)
		exit()

	#parse command line arguments 	
	for i in range(2,len(sys.argv)): 
		if sys.argv[i] == "-v": 
			verbose = 1
		
		elif sys.argv[i] == "-k":
			passkey = sys.argv[i+1]
		
		elif i+1 == len(sys.argv):
			file = sys.argv[i]

	with open (file, "r") as myfile:
		string = myfile.read().replace('\n', '')

	print ("Passkey: ",passkey)

	if encrypt:
		encrypt = Encrypt(string,passkey)
		print ("Encrypt: ",encrypt)
	else:
		decrypt = Decrypt(string,passkey)
		print ("Decrypt: ",decrypt)

if __name__ == "__main__":
	Main()
