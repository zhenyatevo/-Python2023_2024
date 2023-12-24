# (1) Граматическое преобр., постр SA (5б.)
# (2) Преобр SA в транслятор строящий ОПЗ (5б.)
# (3) Интерпритатор ОПЗ (10б.)

def is_valid_expression(expression):
    if not expression:# Проверка на пустую строку
        return False

    balance = 0 # для проверки скобок
    operators = set("+-*/") #Используемые операторы
    digits = set("123456789") #Список цифр для поверки на наличие др. символов
    last_char = None # для проверки на подряд идущ. операторы и числа

    for char in expression: # Проверка на корректность расстановки скобок и правильность символов
        if char == '(': #проверка усл. корректной скобочной посл-ти
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
        elif (char not in operators) and (char not in digits) and (char != '(') and (char != ')'):
            return False # Недопустимый символ
        if (last_char in operators) and (char in operators): # Два оператора подряд
            return False
        if last_char and last_char in digits and char in digits: # Два числа подряд без оператора между ними
            return False
        if last_char == '(' and char == '-': # Отрицательное число в выражении в скобках
            return False
        last_char = char

    if balance != 0: # Несбалансированные скобки
        return False

    if expression[-1] in operators: # Выражение заканчивается оператором
        return False

    #if expression[0] in operators - set('-'): # Выражение начинается с *,/.+
    if expression[0] in operators: #выр нач-ся с оператора
        return False

    return True

# Примеры тестирования
str1 = "(1*(2/3-4))"
str2 = "(3-5)-4"
str3 = "(-3+2)"
str4= "-(3+2)"
str5= "33+2"

print(is_valid_expression(str1))
print(is_valid_expression(str2))
print(is_valid_expression(str3))
print(is_valid_expression(str4))
print(is_valid_expression(str5))








