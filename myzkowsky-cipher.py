# Function to generate new keyword format for encryption process
def getKeyword(keyword):
	keyword = keyword.upper().replace(" ", "")
	listKeyword = []
	for i in range(len(keyword)):
		character = keyword[i]
		if (keyword[i] in listKeyword):
			newCharacter = ''
			for i in range(i-keyword.index(character)):
				newCharacter += character
			listKeyword.append(newCharacter)
		else:
			listKeyword.append(character)
	return listKeyword

# Function to generate matrix for encryption process using keyword and plaintext
def getMatrix(keyword, plaintext):
	plaintext = plaintext.upper().replace(" ", "")
	listPlaintext = []
	for character in plaintext:
		listPlaintext.append(character)
	matrix = [listPlaintext[i:i+len(keyword)] for i in range(0, len(listPlaintext), len(keyword))]
	if (matrix[len(matrix)-1] != len(keyword)):
		for i in range(len(keyword) - len(matrix[len(matrix)-1])):
			matrix[len(matrix)-1].append('X')
	return matrix

# Function to encrypt plaintext
def encrypt(keyword, plaintext):
	keyword = getKeyword(keyword)
	matrix = getMatrix(keyword, plaintext)
	
	listCipherChar = []
	column = 0
	while column < len(keyword):
		cipherChar = ''
		for i in range(len(matrix)):
			cipherChar += matrix[i][column]
		column += 1
		listCipherChar.append(cipherChar)

	dictionaryCipherChar = dict()
	for i in range(len(keyword)):
		dictionaryCipherChar[keyword[i]] = listCipherChar[i]

	dictionaryCipherChar = sorted(dictionaryCipherChar.items())

	ciphertext = ''
	for key, value in dictionaryCipherChar:
		ciphertext += value

	return ciphertext


# Main program
keyword = 'wordkey'
plaintext = 'this is plaintext'

ciphertext = encrypt(keyword, plaintext)
print(ciphertext)
