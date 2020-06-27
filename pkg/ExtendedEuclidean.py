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
        big_list = []
        small_list = []
        remainder = []
        small_coefficient_list = []
        while small != 0:
            big_list.append(big)
            small_list.append(small)
            small_coefficient_list.append(big // small)
            remainder.append(big % small)
            big, small = small, big % small
        for i in range(len(big_list)):
            print("%d = %d * %d + %d" % (big_list[i], small_coefficient_list[i], small_list[i], remainder[i]))
        big_list.pop()
        small_list.pop()
        remainder.pop()
        small_coefficient_list.pop()

        top = len(big_list) - 1
        print("  %d" % remainder[top])
        print("= %d - %d * %d" % (big_list[top], small_coefficient_list[top], small_list[top]))


        return None, None


def main():
    ExtendedEuclidean(100, 19)


if __name__ == '__main__':
    main()


