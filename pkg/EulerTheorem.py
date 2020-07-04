"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
import base
import math


class EulerTheorem(base.Process, base.Value):
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        if math.gcd(a, p) == 1:
            self.p = p
            self.fp = f(p)
        else:
            self.p = -1

    def process(self):
        a = self.a
        b = self.b
        p = self.p
        fp = self.fp
        result = "$$ \\begin{aligned} &\\because \\varphi({" + str(p) + "}) = " + str(fp) + "\\\\"
        result += "&\\therefore {a}^{\\varphi({p})} \equiv {" + str(a) + "}^{" + str(fp) + "}\;mod\;{" + str(p) + "} \\end{alignd} \\\\"



    def value(self):
        a = self.a
        b = self.b
        p = self.p
        fp = self.fp
        b = b % fp
        return a ** b % p


def f(p):
    result = 0
    for i in range(1, p):
        if math.gcd(i, p) == 1:
            result += 1
    return result


def main():
    pass


if __name__ == '__main__':
    main()

