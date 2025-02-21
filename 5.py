#1
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def __repr__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матриці повинні мати однакові розміри для додавання")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матриці повинні мати однакові розміри для віднімання")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])

print("Матриця 1:")
print(matrix1)
print("\nМатриця 2:")
print(matrix2)

print("\nДодавання матриць:")
print(matrix1 + matrix2)

print("\nВіднімання матриць:")
print(matrix1 - matrix2)

matrix3 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix4 = Matrix([[7, 8, 9], [10, 11, 12]])

print("\nМноження матриць:")
print(matrix3 * matrix4)


#2
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)

    def __repr__(self):
        return f"[{self.point1} - {self.point2}]"

class Triangle:
    def __init__(self, point1, point2, point3):
        self.side1 = Segment(point1, point2)
        self.side2 = Segment(point2, point3)
        self.side3 = Segment(point3, point1)

    def perimeter(self):
        return self.side1.length() + self.side2.length() + self.side3.length()

    def __repr__(self):
        return f"Triangle({self.side1}, {self.side2}, {self.side3})"

p1 = Point(0, 0)
p2 = Point(3, 0)
p3 = Point(0, 4)

segment = Segment(p1, p2)
print("Довжина відрізка:", segment.length())

triangle = Triangle(p1, p2, p3)
print("Периметр трикутника:", triangle.perimeter())


#3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name

    def __repr__(self):
        return f"{self.name}, {self.age} років"

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __repr__(self):
        return f"{self.name}, {self.age} років, {self.university}, середній бал: {self.average_grade():.2f}"

student = Student("Іван", 20, "КНУ")
print(student)

student.add_grade(90)
student.add_grade(85)
student.add_grade(78)
print(student)

student.change_name("Іван")
print(student)


#4
class Order:
    def __init__(self, items):
        self.__items = items  

    def get_total_price(self):
        return sum(quantity * price for _, quantity, price in self.__items)

    def get_items(self):
        return self.__items.copy()

class Customer:
    def __init__(self, name):
        self.name = name
        self.__orders = []

    def place_order(self, items, processor):
        order = Order(items)
        self.__orders.append(order)
        processor.process_order(self, order)

    def get_orders(self):
        return self.__orders.copy()

class OrderProcessor:
    def process_order(self, customer, order):
        total = order.get_total_price()
        print(f"Замовлення для {customer.name} оброблено. Загальна вартість: {total:.2f} грн")

customer = Customer("Вася")
processor = OrderProcessor()

items = [("Ноутбук", 1, 25000), ("Миша", 2, 500)]
customer.place_order(items, processor)

items2 = [("Клавіатура", 1, 1500)]
customer.place_order(items2, processor)
