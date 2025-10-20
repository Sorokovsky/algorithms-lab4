def sum_of_digits(number: int) -> int:
    if number < 10:
        return number
    return (number % 10) + sum_of_digits(number // 10)


def main() -> None:
    try:
        number = int(input("Введіть число: "))
        print(f'Кількість цифр числа {number} = {sum_of_digits(number)}')
    except ValueError:
        print("Ви ввели не число")


if __name__ == '__main__':
    main()
