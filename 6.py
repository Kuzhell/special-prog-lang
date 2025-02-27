class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def start_engine(self):
        print("Car engine started")

class Motorcycle(Vehicle):
    def __init__(self, brand, type_):
        super().__init__(brand)
        self.type = type_
    def start_engine(self):
        print("Motorcycle engine started")

class ElectricCar(Car):
    def charge_battery(self):
        print("Battery charging")

class Garage:
    def __init__(self):
        self.vehicles = []
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def start_all_engines(self):
        for v in self.vehicles:
            v.start_engine()

garage = Garage()
garage.add_vehicle(Car("Toyota", "Camry"))
garage.add_vehicle(Motorcycle("Yamaha", "Sport"))
garage.add_vehicle(ElectricCar("Tesla", "Model S"))
garage.start_all_engines()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
    def work(self):
        print(f"{self.name} works as a {self.position}.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def study(self):
        print(f"Student {self.name} with ID {self.student_id} is studying.")

class University:
    def __init__(self):
        self.employees = []
        self.students = []
    def add_employee(self, employee):
        self.employees.append(employee)
    def add_student(self, student):
        self.students.append(student)
    def remove_employee(self, name):
        self.employees = [e for e in self.employees if e.name != name]
    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]
    def find_person(self, identifier):
        for e in self.employees:
            if e.name == identifier:
                return e
        for s in self.students:
            if s.student_id == identifier or s.name == identifier:
                return s
        return None
    def show_info(self):
        for e in self.employees:
            e.introduce()
            e.work()
        for s in self.students:
            s.introduce()
            s.study()

university = University()
university.add_employee(Employee("Zhenia", 20, "Professor"))
university.add_student(Student("Korch", 22, "S123"))
university.show_info()
