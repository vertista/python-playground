class Cat:
    def __init__(self, name):
        self.name = name
        self.is_hungry = True
    def food(self):
        self.is_hungry = False
    def display(self):
        print(f"{self.name} is {self.is_hungry}!")

cat1 = Cat("Mamuk")
cat1.display()
cat1.food()
cat1.display()