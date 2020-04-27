class Point:
    def __init__(self, x, y, z = False):
        self.x = x
        self.y = y
        self.z = z
    def ToString(self):
        if(self.z == False):
            txt = "P({}, {})"
            print(txt.format(round(self.x,2), round(self.y,2)))
        else:
            txt = "P({}, {}, {})"
            print(txt.format(round(self.x,2), round(self.y,2), round(self.z,2)))

P1=Point(2.5555,-3)
P1.ToString()

P2=Point(2,3)
P2.ToString()