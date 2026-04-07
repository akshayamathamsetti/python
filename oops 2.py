class Convert:
    def read_inches(self,inches):
        self.inches=inches
    def to_feet(self):
        self.feet=self.inches/12
    def display(self):
        print("Inches:",self.inches)
        print("Feet:",self.feet)
c=Convert()
c.read_inches(65)
c.to_feet()
c.display()