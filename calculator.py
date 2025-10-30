import logging

# Настройка логирования
logging.basicConfig(filename='calculator.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def add(a, b):
    result = a + b
    logging.info(f"Сложение: {a} + {b} = {result}")
    return result


def subtract(a, b):
    result = a - b
    logging.info(f"Вычитание: {a} - {b} = {result}")
    return result


def multiply(a, b):
    result = a * b
    logging.info(f"Умножение: {a} * {b} = {result}")
    return result


def divide(a, b):
    try:
        result = a / b
        logging.info(f"Деление: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Ошибка: деление на ноль")
        return "Ошибка: деление на ноль"


def main():
    print("Простой калькулятор")
    print("Операции: +, -, *, /")

    while True:
        try:
            a = float(input("Введите первое число: "))
            op = input("Введите операцию: ")
            b = float(input("Введите второе число: "))

            if op == '+':
                print("Результат:", add(a, b))
            elif op == '-':
                print("Результат:", subtract(a, b))
            elif op == '*':
                print("Результат:", multiply(a, b))
            elif op == '/':
                print("Результат:", divide(a, b))
            else:
                print("Неизвестная операция")

        except ValueError:
            print("Ошибка: введите число!")

        cont = input("Продолжить? (y/n): ").lower()
        if cont != 'y':
            break


if __name__ == "__main__":
    main()
