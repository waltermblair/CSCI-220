print("This program will encode and decode your message")

message_fileName=input("Type the name of the file you want to encrypt below\n")
message_encrypted_fileName=input("Type the name of the encryption file below\n")
key=eval(input("Pick a key, 1-25: "))

message_file=open(message_fileName,"r")
message_encrypted_file=open(message_encrypted_fileName,"w")

message_string=message_file.read()

message_encrypted=[]

#Just convert every character in the original string, including spaces.
#No need to make into a list first. Just append all characters to a new list
for ch in message_string:
    if(ord(ch)>96 & ord(ch)<97+26):
        message_encrypted.append(chr((ord(ch)-97+key)%26+97))
    else:
        message_encrypted.append(ch)
   
#A new encrypted string should join together the encrypted list items       
print("".join(message_encrypted), file=message_encrypted_file)

message_encrypted_file.close()

message_encrypted_file2=open("secret_encrypted2.txt","r")
message_decrypted_fileName=input("Time to decrypt. Type the name of the decryption file below\n")
message_decrypted_file=open(message_decrypted_fileName,"w")

encrypted_string=message_encrypted_file2.read()

message_decrypted=[]

for ch in encrypted_string:
    if(ord(ch)>96 & ord(ch)<97+26):
        message_decrypted.append(chr((ord(ch)-97-key)%26+97))
    else:
        message_decrypted.append(ch)

print("".join(message_decrypted), file=message_decrypted_file)

message_file.close()
message_encrypted_file.close()
message_decrypted_file.close()
