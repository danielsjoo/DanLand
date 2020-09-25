class Fruit:
    ripeness = []
    def __init__(self,ripeness):
        self.ripeness.append(ripeness)
    def __str__(self):
        print(self.ripeness)
        return self.ripeness[0]

apple = Fruit("ripe")
print(apple)
banana = Fruit("rotten")
print(banana)
print(apple)