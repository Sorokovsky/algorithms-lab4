from random import randint


def hoar_sort(items: list) -> None:
    if len(items) < 1:
        return
    barrier = items[0]
    l = []
    m = []
    r = []
    for item in items:
        if item < barrier:
            l.append(item)
        elif item == barrier:
            m.append(item)
        else:
            r.append(item)
            hoar_sort(l)
            hoar_sort(r)
    k = 0
    for item in l + m + r:
        items[k] = item
        k += 1


def main() -> None:
    n = 20
    items = []
    for i in range(n):
        items.append(randint(1, 99))
    print(f"Невідсортований масив: {items}")
    hoar_sort(items)
    print(f"Відсортований масив: {items}")


if __name__ == '__main__':
    main()
