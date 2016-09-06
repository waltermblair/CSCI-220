print("This program provides nth term of fibonacci sequence")

n=eval(input("Which term do you want to find?"))

def fib(n):
    a=1
    b=0
    for i in range(n):
        a,b = a+b,a      #Don't forget about simultaneous operations!
    return b

def main():
    print("nth value is: ",fib(n))
main()
