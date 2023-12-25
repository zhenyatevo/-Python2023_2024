#Шаг один (1)
def is_valid_expression(input_string):
    global index
    index = 0
    try:
        parse_expression(input_string)  # Парсинг выражения
        if index == len(input_string):  # Если индекс достиг конца строки, то выражение корректно
            return True
        else:
            return False
    except SyntaxError:
        return False

def parse_expression(input_string):
    parse_term(input_string)  # Парсинг терма
    parse_expression_prime(input_string)  # Парсинг дополнительных выражений

def parse_expression_prime(input_string):
    global index
    # Проверяем, что индекс находится в пределах строки и текущий символ является оператором "+" или "-"
    if index < len(input_string) and (input_string[index] == '+' or input_string[index] == '-'):
        index += 1
        parse_term(input_string)  # Парсинг терма
        parse_expression_prime(input_string)  # Парсинг дополнительных выражений

def parse_term(input_string):
    parse_factor(input_string)  # Парсинг фактора
    parse_term_prime(input_string)  # Парсинг дополнительных термов

def parse_term_prime(input_string):
    global index
    # Проверяем, что индекс находится в пределах строки и текущий символ является оператором "*" или "/"
    if index < len(input_string) and (input_string[index] == '*' or input_string[index] == '/'):
        index += 1
        parse_factor(input_string)  # Парсинг фактора
        parse_term_prime(input_string)  # Парсинг дополнительных термов

def parse_factor(input_string):
    global index
    # Проверяем, что индекс находится в пределах строки и текущий символ является цифрой
    if index < len(input_string) and input_string[index].isdigit():
        index += 1
    # Проверяем, что индекс находится в пределах строки и текущий символ является открывающей скобкой
    elif index < len(input_string) and input_string[index] == '(':
        index += 1
        parse_expression(input_string)  # Парсинг выражения в скобках
        # Проверяем, что индекс находится в пределах строки и текущий символ является закрывающей скобкой
        if index < len(input_string) and input_string[index] == ')':
            index += 1
        else:
            raise SyntaxError("Неправильное выражение: ожидалась закрывающая скобка")
    else:
        raise SyntaxError("Неправильное выражение: ожидалось число или открывающая скобка")





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




# Часть (3), Вычисление выражения
def calculate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():  # Если элемент - число, добавляем его в стек
            stack.append(int(token))
        else:  # Если элемент - оператор, выполняем операцию
            # Извлекаем два последних числа из стека
            right = stack.pop()
            left = stack.pop()
            # Выполняем операцию в зависимости от оператора
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero.")
                stack.append(left / right)
            else:
                raise ValueError(f"Unknown operator: {token}")

    if len(stack) != 1: # Результат - 1 число в стеке
        raise ValueError("Invalid expression.")
    return stack[0]




#Тестирование
str1 = str(input())
if(is_valid_expression(str1)):
    print(True)
    #вызов 2 части, где строится ОПЗ
    print("Было:",str1)
    print("Стало:",infix_to_postfix(str1))
    # вызов 3 части, вычисление
    expression_opz = infix_to_postfix(str1)
    print(calculate_postfix(expression_opz))

else:
    print(False)





