# Shifting the character based on n
def shifting(character, n, options):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	character = character.upper()
	if (options == "encrypt"):
		if character in alphabet:
			index = (alphabet.index(character)+n) % 26
			return alphabet[index]
		else:
			return False
	elif (options == "decrypt"):
		if character in alphabet:
			index = (alphabet.index(character)-n) % 26
			return alphabet[index]
		else:
			return False
	else:
		return False

# Main function to encrypt the plaintext or decrypt the ciphertext, just use options "encrypt" or "decrypt"
def caesar(text, n, options):
	text = text.replace(" ", "")
	result = ''
	for character in text:
		result += shifting(character, n, options)
	return result


plaintext = "this is plaintext"
n = 5

# Encrypt the plaintext using option "encrypt"
ciphertext = caesar(plaintext, n, "encrypt")
print(ciphertext)

# Decrypt the ciphertext using option "decrypt"
plaintext = caesar(ciphertext, n, "decrypt")
print(plaintext)
