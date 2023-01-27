#!/usr/bin/env python3

import argparse, string

ALPHA = string.ascii_uppercase

# Parse args

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-m',
					help="1: Decrypt with a key\n2: Decrypt without a key\n3: Encrypt using a key",
					dest='mode',
					required=True,
					type=int
					)
parser.add_argument('-c',
					help='File containing cipher text',
					dest='cipherFile'
					)
parser.add_argument('-p',
					help='File containing plain text',
					dest='plainFile'
					)
parser.add_argument('-k',
					help='File containing key to decrypt/encrypt text',
					dest='key'
					)
parser.add_argument('-a',
					help='Provide specific alphabet',
					dest='alpha'
					)
parser.add_argument('-g',
					help='Generate new alphabet based on cipher text, [works best on long cipher text]',
					dest='genAlpha',
					action='store_true'
					)
args = parser.parse_args()

#################################
#			Read file 			#
#################################

def readFile(fname):
	try:
		with open(fname, 'r') as ifile:
			return ifile.read().strip()
	except:
		print(f"Error reading file {fname}")
		exit(1)

#################################
#		Get alphabet			#
#################################

def getAlpha(text):
	exist = ""
	notexist = ""
	for char in ALPHA:
		if char in text:
			exist += char
	return exist

#################################
#		Decrypt with a key  	#
#################################

def decryptWithKey(cipher, key):
	if args.alpha:
		alpha = args.alpha.upper()
	elif args.genAlpha:
		alpha = getAlpha(cipher)
	else:
		alpha = ALPHA
	decrypted = ""
	skipped = 0
	for i, char in enumerate(cipher):
		try:
			if char.isalpha():
				new_char_index = alpha.index(char.upper()) - alpha.index(key[(i - skipped) % len(key)].upper()) % len(alpha)
				if char.isupper():
					decrypted += alpha[new_char_index].upper()
				if char.islower():
					decrypted += alpha[new_char_index].lower()
			else:
				skipped += 1
				decrypted += char
		except:
			print("Forbidden characters were found that were not in the provided alphabet")
			exit(1)
	return decrypted

#################################
#		Encrypt with a key 		#
#################################

def encryptWithKey(plain, key):
	print("TODO")

#################################
#		Decrypt without key 	#
#################################

def decryptWithoutKey(cipher):
	print("TODO")

#################################
#		Main					#
#################################

def main():
	if args.mode == 1:
		# Validate user input
		if not args.cipherFile or not args.key:
			print(f"Example: {parser.prog} -m 1 -c cipher.txt -k key.txt")
			exit(1)

		# Read user-provided fiels
		cipher = readFile(args.cipherFile)
		key = readFile(args.key)

		decrypted = decryptWithKey(cipher, key)
		print(decrypted)

#################################
#		Kick off!				#
#################################

if __name__ == "__main__":
	main()