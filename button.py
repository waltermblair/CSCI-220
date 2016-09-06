#button.py
from graphics import *

class Button:

    """A button is a labeled rectangle in a window. It is activated or
    deactivated with the activate() and deactivate() methods. The clicked(p)
    method returns true if the button is active and p is inside it."""
    
    def __init__(self, win, center, width, height, label):
        """Creates a rectangular button, eg:
        qb = Button(mywin, centerPoint, width, height, 'Quit')"""

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgrey')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def clicked(self, p):
        "Returns true if button is active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Return the label string of this button."
        return self.label.getText()
    
class CButton:
    """A button is a labeled circle in a window. It is activated or
    deactivated with the activate() and deactivate() methods. The clicked(p)
    method returns true if the button is active and p is inside it."""
    
    def __init__(self, win, center, radius, label):
        """Creates a rectangular button, eg:
        qb = Button(mywin, centerPoint, width, height, 'Quit')"""

        r=radius
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+r, x-r
        self.ymax, self.ymin = y+r, y-r
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.circ = Circle(Point(x,y),r)
        self.circ.setFill('lightgrey')
        self.circ.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.circ.setWidth(1)
        self.active = False

    def clicked(self, p):
        "Returns true if button is active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Return the label string of this button."
        return self.label.getText()
    
