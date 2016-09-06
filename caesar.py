print("This program will encode and decode your message")

message_string=input("Type your secret message below\n").lower()
key=eval(input("Pick a key, 1-25: "))

message_encrypted=[]

#Just convert every character in the original string, including spaces.
#No need to make into a list first. Just append all characters to a new list
for ch in message_string:
    if(ord(ch)>96 & ord(ch)<97+26):
        message_encrypted.append(chr((ord(ch)-97+key)%26+97))
    else:
        message_encrypted.append(ch)
   
#A new encrypted string should join together the encrypted list items       
print("".join(message_encrypted))

encrypted_string=input("Now time to decode - type your encrypted message below\n")
decryption_key=eval(input("Type your key, 1-25: "))

message_decrypted=[]

for ch in encrypted_string:
    if(ord(ch)>96 & ord(ch)<97+26):
        message_decrypted.append(chr((ord(ch)-97-key)%26+97))
    else:
        message_decrypted.append(ch)

print("".join(message_decrypted))
