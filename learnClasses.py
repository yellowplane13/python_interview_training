class Person:
    def __init__(self, x, y):
        self.name = x
        self.age = y
    
    def bark(self):
        print("woof")
    def get_name(self):
        return self.name
    
    def set_age(self, y):
        self.age = y

man = Person("Tim",12)
print(man.get_name())
man.bark()
man.set_age(123)
print(man.age)