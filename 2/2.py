#!/python/python3.4/bin/python3
import re

## Function: recognize_characters
#  Description: find the characters that are different
#  Parameters: input_file
#      input_file: file path to string to discover
def recognize_characters(input_file):
    with open("input") as input_file:
        str_input  = input_file.read()
    recognized_characters = re.findall("[a-z]", str_input)
    recognized_characters = "".join(recognized_characters)
    
    return recognized_characters

print("You next page is http://www.pythonchallenge.com/pc/def/%s.html" % (recognize_characters("input")))
