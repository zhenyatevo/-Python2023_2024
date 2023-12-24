# (1) Граматическое преобр., постр SA (5б.)
# (2) Преобр SA в транслятор строящий ОПЗ (5б.)
# (3) Интерпритатор ОПЗ (10б.)


# Шаг (2) делаем ОПЗ
def get_precedence(op):
    precedences = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedences.get(op, 0)  # Возвращает 0, если оператора нет в словаре

def is_operator(c):
    return c in '+-*/'

def infix_to_postfix(expression):
    result = []# Результат в ОПЗ
    stack = []    # Стек для хранения операторов

    for char in expression:
        if char.isdigit():
            # Если символ является однозначным числом, добавляем его в результат
            result.append(char)
        elif is_operator(char):
            # Если символ является оператором, выталкиваем из стека все операторы
            # с большим или равным приоритетом в результат
            while stack and get_precedence(char) <= get_precedence(stack[-1]):
                result.append(stack.pop())
            stack.append(char)
        elif char == '(': # Если символ - открывающая скобка, помещаем его в стек
            stack.append(char)
        elif char == ')':
            # Если символ - закрывающая скобка, выталкиваем все операторы из стека
            # до встречи открывающей скобки, которую мы удаляем из стека
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Удаляем открывающую скобку из стека

    # После прохода по всему выражению, выталкиваем все оставшиеся операторы из стека в результат
    while stack:
        result.append(stack.pop())

    return ' '.join(result)    # Преобразуем список в строку и возвращаем




#Шаг один (1)
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



#Тестированиеы
str1 = "(1*(2/3-4))"
if(is_valid_expression(str1)):
    print(True)
    #вызов 2 части, где строится ОПЗ
    print("Было:",str1)
    print("Стало:",infix_to_postfix(str1))
else:
    print(False)




