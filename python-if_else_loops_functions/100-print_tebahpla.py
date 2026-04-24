#!/usr/bin/python3
result = ""

for i in range(26):
    letter_position = 25 - i

    if i % 2 == 0:
        result += chr(97 + letter_position)
    else:
        result += chr(65 + letter_position)

print("{}".format(result), end="")
