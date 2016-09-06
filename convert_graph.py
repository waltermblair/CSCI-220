from graphics import *

#Draw interface
win=GraphWin("Temperature Converter",400,400)
win.setCoords(0,0,100,100)
Text(Point(30,90), "Temperature in Celsius: ").draw(win)
Text(Point(30,20), "Temperature in Fahrenheit: ").draw(win)
input=Entry(Point(75,90),10)
input.setText("0.0")
input.draw(win)
output=Text(Point(75,20),"32.0")
output.draw(win)
button=Text(Point(50,50),"Convert It")
button.draw(win)
Rectangle(Point(40,40),Point(60,60)).draw(win)

#Wait for mouse click
win.getMouse()

#Do the conversion
x = eval(input.getText())
y = 9/5*x+32

#Display the conversion
output.setText(round(y))
button.setText("Done")

win.getMouse()
win.close()
