""" One small letter, surrounded by EXACTLY three big bodyguards on each of its sides. 
I think this exercise is to find a single lower case surrounded by exactly 3 upper case letters."""
#import the argv from sys to allow the passing of parameters
# 5 Nov 2013 just managed to read in the contents of the file
# Need to find a lower case letter surrounded by exactly 3 uppercase letters on both sides

from sys import argv
#Assign names to the arguments passed to the script when started - script is the name of the python script and filename is the filename passed when the script is called
script, filename = argv

#open the file whose parameter was passed and assign the txt' variable name
source_file = open(filename) # source_file contains the filename and other file info
txt = source_file.read() # The .read() command reads the contents of the file and this is then stored in txt

# This function looks for 3 consecutive chars that are uppercase 
def rotate_word(word, n):
	print("just trying to print a char")
	print(n)
	print(word[:10])
	return
	
print("enter the text")
coded_text = str(txt)
print(coded_text[:103])
print(rotate_word(coded_text, 2))

#prints out a message including the filename
print("Here's your file {} " .format(filename))

#print out the contexts of the file . The read command with no parameters
#print(txt.read())
print("looking for 3 chars in caps")


        
        
        
