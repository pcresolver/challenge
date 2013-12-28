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


def find_upper(text):
    upper_found = []
    position = 0
    for c in text:
        if c.isupper():
            upper_found.append(position)
        position += 1
    return upper_found

def find_upper3(upper):
    found3 = []
    for position in range(len(upper) - 5):
        if upper[position + 2] - upper[position] == 2:
            # print(upper[position], " ", upper[position+1], " ", upper[position+2], "next")
            found3.append(upper[position])
    # print(found3)
    return found3
    
def find_upper6(upper3):
    found6 = []
    for position in range(len(upper3) - 1):
        if upper3[position + 1] - upper3[position] == 4:
            found6.append(upper3[position+3])
    return found6
    
def find_hidden_text(upper6, text):
    hidden_text = []
    for position in range(100):
        print("position ", position, "value: ", upper6[position], "content: ", text[upper6[position]])
        hidden_text.append(text[upper6[position] + 4])
        # print(text[position + 3])
    return hidden_text
    
print("enter the text")
coded_text = str(txt)
print(coded_text[:103])
# print(rotate_word(coded_text, 2))

#prints out a message including the filename
print("Here's your file {} " .format(filename))

print("looking for 3 chars in caps")
upper = find_upper(txt) 
# print(upper)       
upper3 = find_upper3(upper)
print(upper3, len(upper3))
upper6 = find_upper6(upper3)
print(upper6, len(upper6))
hidden_text = find_hidden_text(upper6, txt)
print(hidden_text, len(hidden_text))
print(len(upper), len(upper3), len(upper6), len(hidden_text))