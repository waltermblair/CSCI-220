from graphics import *
print("This program draws a polygon from four mouse clicks")

def main():
    win=GraphWin()
    win.setCoords(0.0,0.0,10.0,10.0)
    xaxis=Line(Point(0.5,1),Point(9.5,1))
    yaxis=Line(Point(0.5,1),Point(0.5,9.5))
    message=Text(Point(5,0.25),"Click any points in the graph")
    xaxis.draw(win)
    yaxis.draw(win)
    message.draw(win)

    p = [[0,0],[0,0],[0,0],[0,0]]

    for i in range(4):
        p[i]=win.getMouse()
        p[i].draw(win)

    polygon=Polygon(p[0],p[1],p[2],p[3])
    polygon.setFill('pink')
    polygon.draw(win)

    message.setText("All done, click anywhere to quit.")
    if win.getMouse():
        win.close()

main()
