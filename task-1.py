def is_perfect_square(n: int) -> bool:
    root = int(n ** 0.5)
    return root * root == n


def task(sequence=None, index: int = 0, first_call: bool = True, has_squares: bool = False):
    if first_call:
        sequence = input("Введіть послідовність чисел: ").split(",")
        if not sequence:
            print(0)
            return
        task(sequence, 0, False, False)
    else:
        if index >= len(sequence):
            if not has_squares:
                print(0)
            return
        try:
            number = int(sequence[index])
            if is_perfect_square(number):
                task(sequence, index + 1, False, True)
                print(number, end=" ")
            else:
                task(sequence, index + 1, False, has_squares)
        except ValueError:
            task(sequence, index + 1, False, has_squares)

def main():
    task()

if __name__ == '__main__':
    main()