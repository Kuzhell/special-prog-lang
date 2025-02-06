#1
def km_to_miles(km):
  """Конвертує кілометри в милі."""
  miles = km * 0.621371
  return miles
km_distance = 5
miles_distance = km_to_miles(km_distance)
print(f"{km_distance} км = {miles_distance:.2f} миль")
#2
import math

def power(base, exponent):
    return math.pow(base, exponent)
  
print(power(2, 5))  
print(power(5, 0))  

#3
def factorial(n):
  if n < 0:
      raise ValueError("Факторіал визначений тільки для невід'ємних чисел")

  result = 1
  for i in range(2, n + 1):
      result *= i

  return result

print(factorial(5))
print(factorial(0))

#4
def factorial(n):
  if n < 0:
      raise ValueError("Факторіал визначений тільки для невід'ємних чисел")
  if n == 0 or n == 1:
      return 1
  return n * factorial(n - 1)

print(factorial(5))
print(factorial(0))

#5
def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

print(capitalize_words("привіт світ"))

#6
def longest_word(text):
  words = text.split()
  return max(words, key=len) if words else ""

text = input("Введіть рядок: ")
print("Найдовше слово:", longest_word(text))

#7  
def word_count(text):
  return len(text.split())

text = input("Введіть рядок: ")
print("Кількість слів:", word_count(text))



