from math import sqrt


def task(old_number: int = 0):
    number = int(input("Введіть число(0 для виходу): "))
    if number != 0:
        task(number)
    square = sqrt(old_number)
    if square.is_integer() and not (number == 0 and old_number == 0):
        print(int(square), end=" ")


def main():
    task()


if __name__ == '__main__':
    main()
