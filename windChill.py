print("This program prints a table of calculated wind chill")

print("Temperature\tWind Speed\tWind Chill")
print("--"*25)

for T in range(-20,70,10):
    for V in range(5,55,5):
        chill=35.74+0.6215*T - 35.75*V**0.16 + 0.4275*T*V**0.16
        print("{0:>10}\t{1:>10}\t{2:>10.0f}".format(T,V,chill))
        
