a, b, c = map(float, input("Введите коэффициенты (a b c): ").split())
if a == 0:
    print("x =", -c / b)
else:
    d = b ** 2 - 4 * a * c
    x = -b / (2 * a)
    if d > 0:
        sqrtd_2a = d ** (1 / 2) / (2 * a)
        print("x1 =", round(x - sqrtd_2a, 9))
        print("x2 =", round(x + sqrtd_2a, 9))
    elif d == 0:
        print("x =", x)
    else:
        print("Нет корней")
