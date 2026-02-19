class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def fullname(self):
        return self.name

    def __str__(self) -> str:
        return f"{self.name} - {self.age}"

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age

    def __gt__(self, other) -> bool:
        return self.age > other.age


p1 = Person("Jack", 30)
print(p1.fullname) # Property

p2 = Person("Jack", 30)
p3 = Person("Dan", 35)

print(p1)  # str(p1)  ->   p1.__str__()
print(str(p1))
print(p1.__str__())
print(p1 == p2)  # p1.__eq__(p2)

# print(p1 < p3)  # p1.__gt__(p2)

people = [Person("Andy", 34), Person("Jason", 43), Person("Kevin", 20)]
for p in sorted(people):
    print(p)
