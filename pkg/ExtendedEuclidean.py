"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
import base


class ExtendedEuclidean(base.Process, base.Value):
    def __init__(self, a, b):
        self.a = abs(a)
        self.b = abs(b)

    def process(self) -> str:
        big = max(self.a, self.b)
        small = min(self.a, self.b)
        remainder = [big, small]
        coefficient = []
        result = "$$ \\begin{aligned} "
        while small != 0:
            remainder.append(big % small)
            coefficient.append(big // small)
            big, small = small, big % small

        for i in range(len(coefficient)):
            result += "{" + str(remainder[i]) + "} &= {"+str(coefficient[i])+"} * {"+str(remainder[i + 1])+"} + {"+str(remainder[i + 2])+"} \\\\"

        result += " \end{aligned} $$ $$ \\begin{aligned} "
        remainder.pop()
        coefficient.pop()
        remainder = remainder[::-1]
        coefficient = coefficient[::-1]
        left = [1]
        right = [-coefficient[0]]
        for i in range(1, len(coefficient)):
            left.append(right[i - 1])
            right.append(left[i] * (-coefficient[i]) + left[i - 1])

        result += "{" + str(remainder[0]) + "}"
        for i in range(len(left)):
            result += " &= ({" + str(left[i]) + "}) * {" + str(remainder[i + 2]) + "} + ({" + str(right[i]) + "}) * {" + str(remainder[i + 1]) + "} \\\\"
            if i < len(left) - 1:
                result += " &= ({" + str(left[i]) + "}) * {" + str(remainder[i + 2]) + "} + ({" + str(right[i]) + "}) * ({"+str(remainder[i + 3])+"} - ({" + str(coefficient[i + 1]) + "}) * {"+str(remainder[i + 2])+"}) \\\\"

        return result + " \end{aligned} $$"

    def value(self):
        big = max(self.a, self.b)
        small = min(self.a, self.b)
        remainder = [big, small]
        coefficient = []
        while small != 0:
            remainder.append(big % small)
            coefficient.append(big // small)
            big, small = small, big % small
        remainder.pop()
        coefficient.pop()
        remainder = remainder[::-1]
        coefficient = coefficient[::-1]
        left = [1]
        right = [-coefficient[0]]
        for i in range(1, len(coefficient)):
            left.append(right[i - 1])
            right.append(left[i] * (-coefficient[i]) + left[i - 1])
        if right[-1] * self.a + left[-1] * self.b == remainder[0]:
            return remainder[0], right[-1], left[-1]
        elif left[-1] * self.a + right[-1] * self.b == remainder[0]:
            return remainder[0], left[-1], right[-1]


def main():
    e = ExtendedEuclidean(8656, 7780)
    print(e.process())


if __name__ == '__main__':
    main()


