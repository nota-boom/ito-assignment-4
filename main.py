import math


def f1(x):
    return x ** 3 - 6 * x ** 2 + 11 * x - 6


def bisection_method(a, b, epsilon):
    if f1(a) * f1(b) >= 0:
        print("On this interval method is not applicable")
        return None
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f1(c) == 0:
            return c
        elif f1(a) * f1(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


res1 = bisection_method(1, 2, 0.000001)
if res1:
    print(f"x0 = {res1:.10f}, f(x0) = {f1(res1):.10f}")


def golden_section_method(f, l, r, eps):
    phi = (1 + math.sqrt(5)) / 2
    resphi = 2 - phi
    x1 = l + resphi * (r - l)
    x2 = r - resphi * (r - l)
    f1 = f(x1)
    f2 = f(x2)
    n = 0
    while abs(r - l) >= eps:
        if f1 < f2:
            r = x2
            x2 = x1
            f2 = f1
            x1 = l + resphi * (r - l)
            f1 = f(x1)
        else:
            l = x1
            x1 = x2
            f1 = f2
            x2 = r - resphi * (r - l)
            f2 = f(x2)
        n += 1
    return (x1 + x2) / 2


def f2(x):
    return (x - 2) ** 2 + 3


res2 = golden_section_method(f2, 0, 5, 0.0001)
print(f"x0 = {res2:.10f}, f(x0) = {f2(res2):.10f}")


def gradient_ascent_method(x0, alpha, N):
    x = x0
    for _ in range(N):
        x = x + alpha * (-2 * x + 4)
    return x


def f3(x):
    return -x ** 2 + 4 * x + 1


res3 = gradient_ascent_method(0, 0.1, 100)
print(f"x0 = {res3:.10f}, f(x0) = {f3(res3):.10f}")
