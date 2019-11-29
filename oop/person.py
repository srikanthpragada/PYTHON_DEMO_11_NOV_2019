class Person:
    def __init__(self, name, age):
        # Object attributes
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):  # obj1 == obj2
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):  # obj1 > obj2
        # print("__gt__")
        return self.age > other.age


p1 = Person("A", 21)
p2 = Person("A", 20)

print(p1 == p2)  # p1.__eq__(p2)

print(p1 > p2)  # p1.__gt__(p2)

persons = [Person("A", 20), Person("B", 25), Person("C", 22)]
for p in sorted(persons):
    print(p)
