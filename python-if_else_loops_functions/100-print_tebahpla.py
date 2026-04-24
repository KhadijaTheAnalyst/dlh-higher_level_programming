#!/usr/bin/python3
result = ""

for i in range(26):
    # Which letter in alphabet (0=a, 1=b, ... 25=z)
    letter_position = 25 - i
    
    # Even or odd?
    if i % 2 == 0:
        # Even: use lowercase (a=97)
        result += chr(97 + letter_position)
    else:
        # Odd: use uppercase (A=65)
        result += chr(65 + letter_position)

print(result, end="")
