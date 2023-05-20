

# Задача № 1:
# Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочкам


def cover_card_number(card_number):
     covered_number = '*' * (len(card_number) - 4) + card_number[-4:]
     return covered_number
 card_number = '5864286345695226'
 covered_card_number = cover_card_number(card_number)
 print(covered_card_number)  # Выведет: ************3456


# Задача № 2:
#
# Напишите функцию, которая проверяет: является ли слово палиндромом

 def is_palindrome(word):
     return word == word[::-1]

 print(is_palindrome("deed")) 
 print(is_palindrome("hello")) 

