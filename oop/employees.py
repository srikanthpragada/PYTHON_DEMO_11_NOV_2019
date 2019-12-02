class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_details(self):
        print("Name   ", self.name)
        print("Salary ", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, hra):
        super().__init__(name, salary)
        self.hra = hra

    def print_details(self):
        super().print_details()
        print("Hra    ", self.hra)


m = Manager("Jack", 100000, 30000)
m.print_details()
