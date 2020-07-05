"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
import Interface
import math


class EulerTheorem(Interface.Process, Interface.Value):
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        if math.gcd(a, p) == 1:
            self.p = p
            self.fp = f(p)
        else:
            self.p = -1

    def process(self) ->str:
        a = self.a
        b = self.b
        p = self.p
        fp = self.fp
        result = "$$ \\begin{aligned} &\\because \\varphi({" + str(p) + "}) = " + str(fp) + "\\\\"
        result += "&\\therefore {a}^{\\varphi({p})} \equiv {" + str(a) + "}^{" + str(fp) + "}\;mod\;{" + str(p) + "} \\\\ \\end{aligned} $$"
        result += "$$ \\begin{aligned} {" + str(a) + "}^{" + str(b) + "} &\equiv "
        result += "{({" + str(a) + "} ^ {" + str(fp) + "})}^{" + str(b // fp) + "} \\times {" + str(a) + "}^{" + str(b % fp) + "}\;mod\;{" + str(p) + "} \\\\"
        result += "&\equiv {" + str(a) + "}^{" + str(b - b // fp * fp) + "}\;mod\;{" + str(p) + "} \\\\"
        result += "&\equiv {" + str(a ** (b % fp) % p) + "}\;mod\;{" + str(p) + "} \\\\ \\end{aligned} $$"
        return result

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
    x = EulerTheorem(7, 1005, 5)
    print(x.value())
    print(x.process())


if __name__ == '__main__':
    main()

