"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
import math
import base
import ExtendedEuclidean


class CongruenceModEquation(base.Value, base.Process):
    def __init__(self, a, b, m, num=1):
        try:
            assert a % num == 0 and b % num == 0 and m % num == 0 and num == math.gcd(math.gcd(a, b), m)
        except AssertionError:
            num = -1
        finally:
            self.a = a
            self.b = b
            self.m = m
            self.num = num

    def process(self) -> str:
        result = "$$ \\begin{aligned} "
        if self.num != 1:
            result += "&\\because (" + ", ".join([str(self.a), str(self.b), str(self.m)]) + ") = " + str(self.num) + "\\\\ &\\therefore"
        result += "{" + str(self.a) + "} {x} \;\equiv\; {" + str(self.b) + "}\;mod\;{" + str(self.m) + "} \\\\"
        a = self.a // self.num
        b = self.b // self.num
        m = self.m // self.num
        result += "&\\therefore{" + str(a) + "} {x} \;\equiv\; {" + str(b) + "}\;mod\;{" + str(m) + "} \\\\ \\end{aligned} $$"
        temp = ExtendedEuclidean.ExtendedEuclidean(a, m)
        result += temp.process()
        t, x, _ = temp.value()
        if t != 1:
            result += "$$ \\begin{aligned} \\because (" + str(a) + ", " + str(m) + ") \\not= 1 \\\\ \\therefore No Solution \\end{aligned} $$"
            return result
        else:
            b = x * b % m
            result += "$$ \\begin{aligned} \\therefore {x} \;&\equiv\; {" + str(b) + "}\;mod\;{" + str(m) + "} \\\\ \\end{aligned} $$ $$\\begin{aligned}\\therefore  "
        for i in range(self.num):
            result += "{x} \;&\equiv\; {" + str(b + i * m) + "}\;mod\;{" + str(self.m) + "} \\\\"
        return result + "\\end{aligned} $$"

    def value(self):
        result = []
        if self.num == -1:
            return result
        a = self.a // self.num
        b = self.b // self.num
        m = self.m // self.num
        temp = ExtendedEuclidean.ExtendedEuclidean(a, m)
        t, x, _ = temp.value()
        if t != 1:
            return result
        else:
            b = x * b % m
        for i in range(self.num):
            result.append(b + i * m)
        return result


def main():
    x = CongruenceModEquation(28, 21, 35, 7)
    print(x.process())


if __name__ == '__main__':
    main()
