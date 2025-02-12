#1
class Common_Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def check(self):
        if self.numerator <= self.denominator:
            print("Дріб є правильним")
            return True
        else:
            print("Дріб є неправильним")
            return False

fraction = Common_Fraction(5, 10)
print(fraction.check())
#2
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

vector1 = Vector(7, 2)
vector2 = Vector(4, 8)

print(vector1 + vector2)  
print(vector1 - vector2)  
#3
class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} було прийнято до зоопарку.")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} було забрано з зоопарку.")
        else:
            print(f"{animal.name} не знайдено в зоопарку.")

    def display_animals(self):
        if self.animals:
            print("Тварини в зоопарку:")
            for animal in self.animals:
                print(f"- {animal.name} ({animal.species})")
        else:
            print("Зоопарк порожній.")

zoo = Zoo()

lion = Animal("Лев", "Барик")
elephant = Animal("Слон", "Шпек")

zoo.add_animal(lion)
zoo.add_animal(elephant)

zoo.display_animals()

zoo.remove_animal(lion)

zoo.display_animals()

#4
class FibonacciContainer:
    def __init__(self, n):
        self.fibonacci_sequence = self.generate_fibonacci(n)

    def generate_fibonacci(self, n):
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < n:
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        return fibonacci_sequence[:n]

    def __len__(self):
        return len(self.fibonacci_sequence)

    def __getitem__(self, index):
        return self.fibonacci_sequence[index]

fib_container = FibonacciContainer(10)

print(f"Довжина контейнера: {len(fib_container)}")

print("Перші 5 чисел Фібоначчі:")
for i in range(5):
    print(fib_container[i], end=" ")

