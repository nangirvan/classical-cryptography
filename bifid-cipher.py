# Function to check if character is integer
def isInteger(character):
	try:
		result = int(character)
		return True
	except:
		return False

# Function to get the bifid square
def getSquare():
	square = [['A', 'B', 'C', 'D', 'E'],['F', 'G', 'H', 'I', 'J'],['K', 'L', 'M', 'N', 'O'],['P', 'Q', 'R', 'S', 'T'],['U', 'V', 'W', 'X', 'Y']]
	return square

# Function to convert character to it's row and column number
def convertToNumber(character):
	square = getSquare()
	character = character.upper()
	row = ''
	column = ''
	if (character == 'Z'):
		character = 'Y'
	for i in range(len(square)):
		if (character in square[i]):
			row = str(i+1)
			column = str(square[i].index(character)+1)
	return [row, column]

# Function to get character from the bifid square
def getCharacter(row, column):
	square = getSquare()
	if (isInteger(row) and isInteger(column)):
		row = int(row) - 1
		column = int(column) - 1
		if (row < len(square) and column < len(square)):
			return square[row][column]
		else:
			return ' '
	return ' '

# Function to encrypt plaintext
def encrypt(plaintext):
	plaintext = plaintext.replace(" ", "")
	row = ''
	column = ''
	for character in plaintext:
		convertedChar = convertToNumber(character)
		row += convertedChar[0]
		column += convertedChar[1]
	cipherNumber = row+column
	ciphertext = ''
	for i in range(0, len(cipherNumber), 2):
		ciphertext += getCharacter(cipherNumber[i], cipherNumber[i+1])
	return ciphertext

# Function to decrypt ciphertext
def decrypt(ciphertext):
	ciphertext = ciphertext.replace(" ", "")
	plainNumber = ''
	for character in ciphertext:
		convertedChar = convertToNumber(character)
		plainNumber += convertedChar[0]
		plainNumber += convertedChar[1]
	row = ''
	for i in range(0, int(len(plainNumber)/2)):
		row += plainNumber[i]
	column = ''
	for i in range(int(len(plainNumber)/2), len(plainNumber)):
		column += plainNumber[i]
	ciphertext = ''
	for i in range(len(row)):
		ciphertext += getCharacter(row[i], column[i])
	return ciphertext


# Main program
plaintext = "this is plaintext"

ciphertext = encrypt(plaintext)
print(ciphertext)

plaintext = decrypt(ciphertext)
print(plaintext)
