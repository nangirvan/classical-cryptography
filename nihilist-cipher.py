# Function to split string into some array parts
def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]

# Function to check if character is integer
def isInteger(character):
	try:
		result = int(character)
		return True
	except:
		return False

# Function to generate square using keyword
def generateSquare(keyword):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	keyword = keyword.upper()
	listKeyword = []
	for character in keyword:
		if (character not in listKeyword):
			listKeyword.append(character)
	listAllCharacter = listKeyword
	for character in alphabet:
		if (character not in listKeyword):
			listAllCharacter.append(character)	
	return [listAllCharacter[i:i+5] for i in range(0, len(listAllCharacter), 5)]

# Function to generate key based on text length
def generateKey(lenText, key):
	key = key.upper()
	if (lenText > len(key)):
		length = lenText - len(key)
		for x in range(length):
			key += key[x]
		return key
	elif (lenText < len(key)):
		length = len(key) - lenText
		return key[:-length]
	else:
		return key

# Function to get index of character in square
def findIndex(character, square):
	character = character.upper()
	for i in range(len(square)):
		if (character in square[i]):
			row = str(i+1)
			column = str(square[i].index(character)+1)
			return row+column

# Function to get character in square
def findCharacter(index, square):
	row = index[0]
	column = index[1]
	if (isInteger(row) and isInteger(column)):
		row = int(row)-1
		column = int(column)-1
		return square[row][column]
	else:
		return " "

# Function to encrypt plaintext
def encrypt(keyword, plaintext, key):
	plaintext = plaintext.replace(" ", "")
	keyword = keyword.replace(" ", "")
	key = key.replace(" ", "")

	square = generateSquare(keyword)
	key = generateKey(len(plaintext), key)
	
	indexPlaintext = []
	for character in plaintext:
		indexPlaintext.append(int(findIndex(character, square)))
	
	indexKey = []
	for character in key:
		indexKey.append(int(findIndex(character, square)))

	ciphertext = ""
	for i in range(len(indexPlaintext)):
		character = indexPlaintext[i]+indexKey[i]
		if (character > 100):
			character -= 100
			if (character < 10):
				character = "0"+str(character)
		ciphertext += str(character)

	return ciphertext

# Function to decrypt ciphertext
def decrypt(keyword, ciphertext, key):
	ciphertext = ciphertext.replace(" ", "")
	keyword = keyword.replace(" ", "")
	key = key.replace(" ", "")

	square = generateSquare(keyword)
	key = generateKey(int(len(ciphertext)/2), key)

	indexKey = ""
	for character in key:
		indexKey += findIndex(character, square)

	key = split(indexKey, 2)
	ciphertext = split(ciphertext, 2)

	indexPlaintext = []
	for i in range(len(key)):
		if (isInteger(ciphertext[i]) and isInteger(key[i])):
			indexCiphertext = int(ciphertext[i])
			indexKey = int(key[i])
			if (indexCiphertext < 10):
				indexCiphertext += 100
			indexPlaintext.append(str(indexCiphertext - indexKey))

	plaintext = ""
	for index in indexPlaintext:
		character = findCharacter(index, square)
		plaintext += character

	return plaintext


# Main program
keyword = "wordkey"
plaintext = "this is plaintext"
key = "secret"

ciphertext = encrypt(keyword, plaintext, key)
print(ciphertext)

plaintext = decrypt(keyword, ciphertext, key)
print(plaintext)
