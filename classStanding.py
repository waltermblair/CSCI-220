c=eval(input("How many credits have been earned? "))

if c >= 26:
    s="Senior"
elif c>=16 and c<26:
    s="Junior"
elif c>=7 and c<16:
    s="Sophomore"
else:
    s="Freshman"

print(s)
