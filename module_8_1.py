def add_everything_up(a, b):
    try:
        # Если оба аргумента — числа (int или float), то их складываем.
        result = a + b
        if isinstance(result, float):
            return f"{result:.3f}"  # Форматирование до 3 знаков после запятой
        return result
    except TypeError:
        # Если происходит TypeError (разные типы), возвращаем строковое представление a и b.
        return str(a) + str(b)

# Пример использования функции:
print(add_everything_up(123.456, 'строка'))  # Ожидается вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Ожидается вывод: яблоко4215
print(add_everything_up(123.456, 7))  # Ожидается вывод: 130.456
