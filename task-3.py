from random import randint
from time import time


def hoar_sort(items: list, random_barrier: bool = False) -> None:
    if len(items) < 1:
        return
    barrier_index = randint(0, len(items) - 1) if random_barrier else 0
    barrier = items[barrier_index]
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


def avarage(times: float) -> float:
    return sum(times) / len(times)

def main() -> None:
    n = 25
    count = 100
    non_random_metric = []
    random_metric = []
    for i in range(count):
        items = [randint(1, 100) for _ in range(n)]
        by_random_start = time()
        by_random_sort = hoar_sort(items.copy(), True)
        by_random_end = time()
        by_not_random_start = time()
        random_metric.append(by_random_end - by_random_start)
        by_not_random_sort = hoar_sort(items.copy(), False)
        by_not_random_end = time()
        non_random_metric.append(by_not_random_end - by_not_random_start)
        print(f"Вхідний масив на {i + 1} ітерації: {items}")
        print(f"Час із першим бар'єром: {by_not_random_end - by_not_random_start}")
        print(f"Час із випадковим бар'єром: {by_random_end - by_random_start}")

    print(f"В середньому з сталим: {avarage(non_random_metric)}")
    print(f"В середньому з випадковим: {avarage(random_metric)}")

if __name__ == '__main__':
    main()
