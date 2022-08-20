"""
Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format.
"""

octal_number='0o25'
hex_number='0x39'
print(bin(int(octal_number[2::])+int(hex_number[2::])))