"""
Encrypt this!

Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter needs to be converted to its ASCII code.
The second letter needs to be switched with the last letter
Keepin' it simple: There are no special characters in input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"

"""

def encrypt_this(text):
    crypt = []
    for word in text.split():
        if len(word) == 1:            
            crypt.append(str(ord(word[0])))
        elif len(word) == 2:
            crypt.append(f'{ord(word[0])}{word[1]}')
        else:
            crypt.append(f'{ord(word[0])}{word[-1]}{word[2:-1]}{word[1:2]}')        
    return ' '.join(crypt)