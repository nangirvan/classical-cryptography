# Function to get index of character in matrix
def findIndex(character, matrix):
	index = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if (character == matrix[i][j]):
				index.append(i)
				index.append(j)
	return index

# Function to convert character to adfgvx character
def convertIndex(index):
	if (index == 0):
		return 'A'
	elif (index == 1):
		return 'D'
	elif (index == 2):
		return 'F'
	elif (index == 3):
		return 'G'
	elif (index == 4):
		return 'V'
	elif (index == 5):
		return 'X'
	else:
		return False

# Function to encode plaintext using adfgvx matrix
def encode(plaintext, matrix):
	plaintext = plaintext.upper().replace(" ", "")
	encodeText = ''
	for character in plaintext:
		index = findIndex(character, matrix)
		encodeChar = convertIndex(index[0]) + convertIndex(index[1])
		encodeText += encodeChar
	return encodeText

# Function to remove same character from keyword 
def getKeyword(keyword):
	keyword = keyword.upper()
	listKeyword = []
	for character in keyword:
		if (character not in listKeyword):
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
	
	keyword.sort()

	ciphertext = ''
	for i in range(len(keyword)):
		ciphertext += dictionaryCipherChar[keyword[i]]

	return ciphertext


# Declare adfgvx matrix, there's many other version of adfgvx matrix
matrix = [['8', 'P', '3', 'D', '1', 'N'],['L', 'T', '4', 'O', 'A', 'H'],['7', 'K', 'B', 'C', '5', 'Z'],['J', 'U', '6', 'W', 'G', 'M'],['X', 'S', 'V', 'I', 'R', '2'],['9', 'E', 'Y', '0', 'F', 'Q']]

# Main program
plaintext = 'this is plaintext'
keyword = 'wordkey'

encodedtext = encode(plaintext, matrix)
ciphertext = encrypt(keyword, encodedtext)
print(ciphertext)
