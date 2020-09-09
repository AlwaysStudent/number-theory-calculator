import math
from pkg import interface


class Jacobi(interface.Process, interface.Value):
    def __init__(self, a, m):
        self.a = a
        self.m = m

    def process(self) -> str:
        value = 1
        a = self.a
        m = self.m
        result = r"$$ \begin{aligned} (\frac{" + \
                 str(a) + \
                 "}{" + \
                 str(m) + \
                 "})"
        while m > 1:
            a = a % m
            temp = m // 2
            result += r" &= (" + \
                      str(value) + \
                      r") \times (\frac{" + \
                      str(a) + \
                      "}{" + \
                      str(m) + \
                      r"}) \\"
            if a > temp:
                a = m - a
                result += r"&= (" + \
                          str(value) + \
                          r") \times (-1)^{\frac{" + \
                          str(m) + \
                          r"}{2}} \times (\frac{" + \
                          str(a) + \
                          "}{" + \
                          str(m) + \
                          r"}) \\"
                if m % 4 == 3:
                    value = -value
                result += r" &= (" + \
                          str(value) + \
                          r") \times (\frac{" + \
                          str(a) + \
                          "}{" + \
                          str(m) + \
                          r"}) \\"
            if a == 0:
                result += r" &= 0 \\"
                value = 0
                break
            while a % 4 == 0:
                a = a // 4
                result += r" &= (" + \
                          str(value) + \
                          r") \times {(-1)^{\frac{{" + \
                          str(m) + \
                          r"}^{2}}{8}}}^{2} \times (\frac{" + \
                          str(a) + \
                          "}{" + \
                          str(m) + \
                          r"}) \\"
                result += r" &= (" + \
                          str(value) + \
                          r") \times (\frac{" + \
                          str(a) + \
                          "}{" + \
                          str(m) + \
                          r"}) \\"
            if a % 2 == 0:
                a = a // 2
                result += r" &= (" + \
                          str(value) + \
                          r") \times (-1)^{\frac{{" + \
                          str(m) + \
                          r"}^{2}}{8}} \times (\frac{" + \
                          str(a) + \
                          "}{" + \
                          str(m) + \
                          r"}) \\"
                if m % 8 == 3 or m % 8 == 5:
                    value = -value
                result += r" &= (" + \
                          str(value) + \
                          r") \times (\frac{" + \
                          str(a) + \
                          "}{" + \
                          str(m) + \
                          r"}) \\"
            if a % 4 == 3 and m % 4 == 3:
                value = -value
            temp = a
            a = m
            m = temp
            result += r" &= (" + \
                      str(value) + \
                      r") \times (-1)^{{\frac{" + \
                      str(a) + \
                      r"-1}{2}}\cdot{\frac{" + \
                      str(m) + \
                      r"-1}{2}}} \times (\frac{" + \
                      str(a) + \
                      "}{" + \
                      str(m) + \
                      r"}) \\"
        result += r" &= {" + \
                  str(value) + \
                  "} "
        return result + r"\end{aligned} $$"

    def value(self):
        result = 1
        a = self.a
        m = self.m
        while m > 1:
            _, a = divmod(a, m)
            temp, _ = divmod(m, 2)
            if a > temp:
                a = m - a
                if is_congruent(m, 3, 4):
                    result = -result
            if a == 0:
                result = 0
                break
            while is_congruent(a, 0, 4):
                a, _ = divmod(a, 4)
            if is_congruent(a, 0, 2):
                a, _ = divmod(a, 2)
                if is_congruent(m, 3, 8) or is_congruent(m, -3, 8):
                    result = -result
            if is_congruent(a, 3, 4) and is_congruent(m, 3, 4):
                result = -result
            temp = a
            a = m
            m = temp
        return result


def is_congruent(a, b, n):
    r = (a - b) % n
    if r == 0:
        return True
    else:
        return False


def is_Legendre(e):
    if is_prime(e.m):
        return True
    return False


def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if math.gcd(i, n) != 1:
            return False
    return True


def main():
    x = Jacobi(1233, 5432)
    print(is_Legendre(x))
    print(x.process())


if __name__ == '__main__':
    main()
