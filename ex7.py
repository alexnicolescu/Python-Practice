class Car:
    def __init__(self, year):
        self.year = year
    
    def age(self):
        return self.year


c = Car(2018)
print(c.age())