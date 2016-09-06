print("This program decodes the secret encoder.py message!")

message=input("Please input the secret encoded message below")

output=[]
for i in message.split():
    Num=eval(i)
    output.append(chr(Num))

message="".join(output)

print(message)
