# Function to extract maximum numeric value from a given string
import re

def extractMax(input):

	# get a list of all numbers separated by 
	# lower case characters 
	numbers = re.findall('\d+',input)
	numbers = map(int,numbers)

	print max(numbers)

# Driver program
if __name__ == "__main__":
	input = '923klp543pem263lmn'
	extractMax(input)
