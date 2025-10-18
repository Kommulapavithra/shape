class shape:
    def no_of_sides(self):
        print("This shape has many sides")
class square(shape):
    def no_of_sides(self):
        print("A square has 4sides")
s1 = shape()
s2 = square()
s1.no_of_sides()
s2.no_of_sides()
