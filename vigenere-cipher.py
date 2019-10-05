# Function to set key based on the text
def setKey(text, key):
	text = text.replace(" ", "")
	key = key.replace(" ", "")
	if (len(text) > len(key)):
		length = len(text) - len(key)
		for character in range(length):
			key += key[character]
		return key
	elif (len(text) < len(key)):
		length = len(key) - len(text)
		return key[:-length]
	else:
		return key


# Function to get character based on calculation from 2 character, text and key
def getCharacter(charText, charKey, options):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	charText = charText.upper()
	charKey = charKey.upper()
	if (charText in alphabet and charKey in alphabet):
		if (options == "encrypt"):
			index = (alphabet.index(charText) + alphabet.index(charKey)) % 26
		elif (options == "decrypt"):
			index = (alphabet.index(charText) - alphabet.index(charKey)) % 26
		else:
			return " "
		return alphabet[index]
	else:
		return " "


# Function to encrypt plaintext
def encrypt(plaintext, key):
	plaintext = plaintext.replace(" ", "")
	ciphertext = ""
	key = setKey(plaintext, key)
	for character in range(len(plaintext)):
		ciphertext += getCharacter(plaintext[character], key[character], "encrypt")
	return ciphertext


# Function to decrypt ciphertext
def decrypt(ciphertext, key):
	ciphertext = ciphertext.replace(" ", "")
	plaintext = ""
	key = setKey(ciphertext, key)
	for character in range(len(ciphertext)):
		plaintext += getCharacter(ciphertext[character], key[character], "decrypt")
	return plaintext


# Main program
plaintext = "this is plaintext"
key = "it is key"

ciphertext = encrypt(plaintext, key)
print(ciphertext)

plaintext = decrypt(ciphertext, key)
print(plaintext)
