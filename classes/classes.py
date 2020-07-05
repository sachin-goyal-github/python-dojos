class Greeter(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi "+ self.name)

g1 = Greeter("Sachin")
g1.greet()
g2 = Greeter("Puja")
g2.greet()
