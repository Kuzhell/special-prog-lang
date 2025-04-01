#1
def average_nonnegative(numbers):
    nonnegative_numbers = [num for num in numbers if num >= 0]

    if not nonnegative_numbers:
        return "У списку немає невід'ємних чисел."

    return sum(nonnegative_numbers) / len(nonnegative_numbers)

numbers = list(map(float, input("Введіть числа через пробіл: ").split()))

result = average_nonnegative(numbers)
print("Середнє арифметичне невід'ємних чисел:", result)
#2
def reverse_string(s):
    return s[::-1]
user_input = input("Введіть рядок: ")
print("Реверсований рядок:", reverse_string(user_input))
#3
def reverse_words_in_sentence(s):
    words = s.split()  
    reversed_words = [word[::-1] for word in words] 
    return ' '.join(reversed_words)

user_input = input("Введіть рядок: ")
print("Реверсований рядок:", reverse_words_in_sentence(user_input))
#4
def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    return s == s[::-1]  
input_string = input("Введіть рядок: ")
if is_palindrome(input_string):
    print("Цей рядок є паліндромом.")
else:
    print("Цей рядок не є паліндромом.")
#6
input_string = input("Введіть рядок: ")
unique_chars = set(input_string)
for char in unique_chars:
    count = input_string.count(char)
    print(f"Символ '{char}' зустрічається {count} раз(ів).")
#7
input_dict = {'a': 1, 'b': 2, 'c': 3}
tuple_list = list(input_dict.items())
print(tuple_list)





