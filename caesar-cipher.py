# shifting the character
def shifting(character, n):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	character = character.upper()
	if character in alphabet:
		index = (alphabet.index(character)+n) % 26
		return alphabet[index]
	else:
		return False

# encrypt the plaintext to generate ciphertext using shifting function
def encrypt(plaintext, n):
	ciphertext = ''
	for character in plaintext:
		ciphertext += shifting(character, n)
	return ciphertext



plaintext = input('Enter plaintext : ')
n = input('How many n shifting : ')

if (isinstance(n, int)):
	ciphertext = encrypt(plaintext, n)
	print(ciphertext)
else:
	print('n must be integer')
