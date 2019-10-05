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

# Function to get the square of polybius
def getSquare():
	square = [['A', 'B', 'C', 'D', 'E'],['F', 'G', 'H', 'I', 'K'],['L', 'M', 'N', 'O', 'P'],['Q', 'R', 'S', 'T', 'U'],['V', 'W', 'X', 'Y', 'Z']]
	return square

# Function to get index of character in polybius square
def findIndex(character):
	square = getSquare()
	character = character.upper()
	if (character == 'J'):
		character = 'I'
	for i in range(len(square)):
		for j in range(len(square[i])):
			if (square[i][j] == character):
				return str(i+1)+str(j+1)

# Function to get character from polybius square
def findCharacter(row, column):
	square = getSquare()
	if (isInteger(row) and isInteger(column)):
		row = int(row)
		column = int(column)
		if (row < len(square) and column < len(square)):
			return square[row][column]
		else:
			return " "
	else:
		return "Wrong index format"


# Main function to encrypt plaintext or decrypt ciphertext
def polybius(text, options):
	text = text.replace(" ", "")
	result = ""
	if (options == "encrypt"):
		for character in text:
			result += findIndex(character)
	elif(options == "decrypt"):
		if (len(text) % 2 != 0):
			result = "Wrong ciphertext format"
		else:
			text = split(text, 2)
			for index in text:
				row = int(index[0])-1
				column = int(index[1])-1
				result += findCharacter(row, column)
	else:
		result = "Wrong options"
	return result


# Main program
plaintext = "this is plaintext"

ciphertext = polybius(plaintext, "encrypt")
print(ciphertext)

plaintext = polybius(ciphertext, "decrypt")
print(plaintext)
