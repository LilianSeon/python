class Point:
    def __init__(self, x, y, z = False):
        self.x = x
        self.y = y
        self.z = z
    def ToString(self):
        if(self.z == False):
            txt = "P({} , {})"
            print(txt.format(self.x, self.y))
        else:
            txt = "P({} , {}, {})"
            print(txt.format(round(self.x,2), self.y, self.z))

P1=Point(2.5555,-3,9)
P1.ToString()