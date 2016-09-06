print("This program averages user's numbers")
n=eval(input("How many numbers do you want to average?\t"))
x=0
for i in range(n):
    x=x+eval(input("Enter a number: "))
    avg=x/n
print("Average: ",avg)
