'''
LZW Compressor Program
@author: Sharath Kancharla
'''

import sys

''' Import argparse module to pass command line arguments '''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('bitlength', type = int)
args = parser.parse_args()


bit_length = args.bitlength         # To set a fixed BIT LENGTH from command line argument

if bit_length < 9 or bit_length > 16:  # To check whether the given bit length is in range(9,16)    
    print("Bit length should be >8 and <17")
    sys.exit(0)                         # To exit without showing unnecessary errors in command prompt
else:
    max_table_size= 2**(bit_length)     # To set the MAX TABLE SIZE
    
''' To open and read input text file '''

try:                   
    with open(args.filename,encoding='utf-8') as f: # The filename when passing command line argument should be 'input.txt'
        content = f.read()          # Storing the data in the file as a string in content
    f.close()    
except FileNotFoundError:
    print("Not a valid filename or extension")  # Prints message when an invalid file is passed as command line argument  
    sys.exit(0)
    
'''Encoding Algorithm'''

table = []              # Creating an empty table
for i in range(0,256):
    table.append(chr(i))
    
# Using print(table) outputs list of extended ASCII characters

def get_code(string):           # get_code function returns the code for the string in table
    if string in table:
        return table.index(string)

output = []             # To store the codes in a list 
string= ""
i = 0  
while i < len(content):     # Iteratively reads symbols from content
    symbol = content[i]
    if string + symbol in table:        
        string = string + symbol    
    else:
        output.append(get_code(string))     # Appends codes to output 
        if len(table) < max_table_size:     
            table.append(string+symbol)     # Appends table with string+symbol as a new item
        string = symbol
    i+=1

# Exhauts when there are no more symbols left
    
output.append(get_code(string))     # Appends the last code to output     
                     
print("Encoded Ouput is: ")         # Prints the Encoded output 
print(output)

# Using print(table) outputs updated table 

''' To open and write encoded output in 16-bit format to file '''

fo = open("input.lzw", 'wb')         # Creates a input.lzw file in binary mode 

for code in output:                 
   fo.write(code.to_bytes(2, byteorder='big'))     # Stores each value in a 16-bit format

   # Using print(len(code.to_bytes(2, byteorder='big'))) outputs 2 bytes 

fo.close()   









