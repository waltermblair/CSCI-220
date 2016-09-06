print("This program tells you how shitty your kids are.")

score=eval(input("Quiz score out of 5: "))
grades=["F", "F", "D", "C", "B", "A"]

print("Your shitty kid made a {0}".format(grades[score]))

test=eval(input("Test score out of 100: "))
test_grades=("F"*60+"D"*10+"C"*10+"B"*10+"A"*10)

print("Your shitty kid made a {0}".format(test_grades[test]))
