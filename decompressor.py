'''
LZW Decompressor Program
Name: Sharath Kancharla
'''

import sys

''' Import argparse module to pass command line arguments '''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('bitlength', type = int)
args = parser.parse_args()


bit_length = args.bitlength     # To set a fixed BIT LENGTH from command line argument

if bit_length < 9 or bit_length > 16:  # To check whether the given bit length is in range(9,16) 
    print("Bit length should be >8 and <17")
    sys.exit(0)
else:
    max_table_size= 2**(bit_length)     # To set the MAX TABLE SIZE
    
''' To open and read input lzw file '''
    
try:    
    f = open(args.filename, 'rb')       # The filename when passing command line argument should be 'input.lzw'
except FileNotFoundError:
    print("Not a valid filename or extension")  # Prints message when an invalid file is passed as command line argument
    sys.exit(0)
    
bytes_2 = f.read()  # Stores the bytes data to bytes_2
codes = []          
i= 0
while i < len(bytes_2):     # Iteratively converts 2 bytes at a time to integer value  
    codes.append(int.from_bytes(bytes_2[i:i+2], byteorder='big', signed=False)) 
    i = i+2
f.close()

# Using print(codes) outputs the list of compressor's output   

'''Decoding Algorithm'''

table = []      # Creating an empty table
for i in range(0,256):
    table.append(chr(i))

# Using print(table) outputs list of extended ASCII characters

output = ""
string = ""    
content = ""
string = table[codes[0]]    # Gives ascii character of the first code in codes
content+=string             # Concatenates the string to content
output = string              
i=1
while i < len(codes):       # Iteratively reads each code from codes
    code = codes[i]
    if code >= len(table):  # If code not in table
        new_string = string + string[0]
    else:
        new_string = table[code]
    output = new_string      
    content+=output         # Concatenates the output to content
    if len(table) < max_table_size:
        table.append(string + new_string[0])    # Appends table with string+new_string[0] as a new item
    string = new_string
    i+=1
    
# Exhauts when there are no more codes left
    
print("Decoded output is: " + content)  # Prints the decoded output 

''' To open and write decoded output as a string to file '''

fo = open("input_decoded.txt", 'w')     # Creates a input_decoded.txt file 

fo.write(content)                       # Writes the decoded string to file

fo.close()


