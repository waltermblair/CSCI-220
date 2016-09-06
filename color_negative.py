from graphics import *

print("This program converts a color image to its color negative.")
imageName=input("Name of the image file: ")
width=eval(input("How many pixels wide is image? "))
height=eval(input("How many pixels tall? "))

win=GraphWin("Image Window", width, height)
win.setCoords(0,0,100,100)

image=Image(Point(50,50),imageName)
image.draw(win)
instr=Text(Point(20,95),"Click to convert to color negative")
instr.draw(win)
win.getMouse()
instr.setText("Now we wait...")

#conversion
for x in range(width):
    for y in range(height):
        rgbList=image.getPixel(x,y)
        image.setPixel(x,y,
            color_rgb(255-rgbList[0],255-rgbList[1],255-rgbList[2]))
        win.update()

instr.setText("Enter your new file name in the terminal.")
newFileName=input("Name of the new image file: ")
image.save(newFileName)

instr.setText("Image saved successfully, good work!")
