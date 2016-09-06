print("This program encodes messages into unicode!")

message=input("Type your secret message below\n")

for chr in message:
    print(ord(chr)," ")
