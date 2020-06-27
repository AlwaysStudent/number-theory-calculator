"""
Author: AlwaysStudent
PythonVersion: 3.7
"""


class ExtendedEuclidean:
    def __init__(self, a, b):
        self.a = abs(a)
        self.b = abs(b)
        self.process, self.value = self.__run()

    def __run(self):
        big = max(self.a, self.b)
        small = min(self.a, self.b)
        remainder = [big, small]
        coefficient = []
        while small != 0:
            coefficient.append(big // small)
            remainder.append(big % small)
            big, small = small, big % small
        for i in range(len(coefficient)):
            print("%d = %d * %d + %d" % (remainder[i], coefficient[i], remainder[i + 1], remainder[i + 2]))
        remainder.pop()
        remainder = remainder[::-1]
        coefficient.pop()
        coefficient = [-i for i in coefficient[::-1]]
        print(coefficient)
        temp = [coefficient[0]]
        for i in range(len(coefficient) - 1):
            temp.append(temp[i] * coefficient[i + 1] + 1)
        print(temp)
        print("------------------------------------------------")
        for i in range(len(coefficient)):
            print("%d = %d + (%d) * %d" % (remainder[i], remainder[i + 2], coefficient[i], remainder[i + 1]))
        print("------------------------------------------------")
        print("%d" % remainder[0])
        for i in range(len(coefficient) - 1):
            print("= %d + (%d) * %d" % (remainder[i + 2], temp[i], remainder[i + 1]))
            print("= %d + (%d) * (%d + (%d) * %d)" % (remainder[i + 2], temp[i], remainder[i + 3], coefficient[i + 1], remainder[i + 2]))

        return None, None


def main():
    ExtendedEuclidean(8656, -7780)


if __name__ == '__main__':
    main()


