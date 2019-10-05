# Function to check if character is integer
def isInteger(character):
	try:
		result = int(character)
		return True
	except:
		return False

# Function to get shifted character based on n
def shifting(character, n, options):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	character = character.upper()
	if (character in alphabet):
		if (options == "encrypt"):
			index = (alphabet.index(character)+n) % 26
		elif (options == "decrypt"):
			index = (alphabet.index(character)-n) % 26
		else:
			return " "
		return alphabet[index]
	else:
		return " "

# Function to encrypt plaintext
def encrypt(plaintext, n):
	plaintext = plaintext.replace(" ", "")
	ciphertext = ""
	for character in plaintext:
		ciphertext += shifting(character, n, "encrypt")
	return ciphertext

# Function to decrypt plaintext
def decrypt(ciphertext, n):
	ciphertext = ciphertext.replace(" ", "")
	plaintext = ""
	for character in ciphertext:
		plaintext += shifting(character, n, "decrypt")
	return plaintext



# Main Program
plaintext = "this is plaintext"
n = 5

ciphertext = encrypt(plaintext, n)
print(ciphertext)

plaintext = decrypt(ciphertext, n)
print(plaintext)
