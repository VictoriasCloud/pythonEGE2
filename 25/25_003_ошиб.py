def get_divs(x):
    divs = set()  # создаем множество
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0:  # тут проверяем, является ли d делителем числа ч
            y = d  # для удобства
            if y % 2 == 0:  # проверяем, четный ли делитель
                divs.add(y)  # добавляем
            y = x // d  # для удобства
            if y % 2 == 0:  # проверяем, четный ли делитель
                divs.add(y)  # добавляем
    return sorted(divs)


for x in range(125256, 125330 + 1):
    divs = get_divs(x)

    if len(divs) == 6:
        print(x, sorted(divs))
