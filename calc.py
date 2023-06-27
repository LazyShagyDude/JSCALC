# Функция для вычисления математического выражения
def calculate(expression):
    try:
        # Используем функцию eval() для вычисления выражения
        result = eval(expression)
        return result
    except Exception:
        return "Ошибка: Некорректное выражение"


# Получаем входное выражение от пользователя
expression = input("Введите математическое выражение: ")

# Вычисляем результат и выводим его
result = calculate(expression)
print("Результат:", result)
