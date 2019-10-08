# Function to remove same character from keyword
def getKeyword(keyword):
	keyword = keyword.upper().replace(" ", "")
	listKeyword = []
	for character in keyword:
		if (character not in listKeyword):
			listKeyword.append(character)
	return listKeyword

# Function to generate matrix for encyption process using keyword and plaintext
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

	keyword.sort()

	ciphertext = ''
	for i in range(len(keyword)):
		ciphertext += dictionaryCipherChar[keyword[i]]

	return ciphertext


# Main program
keyword = 'wordkey'
plaintext = 'this is plaintext'

ciphertext = encrypt(keyword, plaintext)
print(ciphertext)
