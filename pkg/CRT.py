from pkg import interface
from pkg import ExtendedEuclidean


class CRT(interface.Process, interface.Value):
    def __init__(self, remainder, mod):
        self.remainder = remainder
        self.mod = mod
        if judge_mod(mod):
            self.length = len(mod)
        else:
            self.length = -1

    def process(self) -> str:
        result = "$$ \\begin{aligned} {m} &= "
        m = 1
        _M_ = []
        _InvM_ = []
        result += " \\times ".join([("{" + str(k) + "}") for k in self.mod])
        for i in range(self.length):
            m *= self.mod[i]
        result += " = " + \
                  str(m) + \
                  "\\\\"
        for i in range(self.length):
            temp = 1
            temp_list = []
            result += "{M_{" + \
                      str(i + 1) + \
                      "}} &= "
            for j in range(self.length):
                if self.mod[i] != self.mod[j]:
                    temp *= self.mod[j]
                    temp_list.append(self.mod[j])
            result += " \\times ".join([("{" + str(k) + "}") for k in temp_list])
            result += " = {" + \
                      str(temp) + \
                      "} \\\\"
            _M_.append(temp)
        result += "\\end{aligned} $$"
        for i in range(self.length):
            temp = ExtendedEuclidean.ExtendedEuclidean(_M_[i], self.mod[i])
            _, x, _ = temp.value()
            result += temp.process()
            _InvM_.append(x % self.mod[i])
            result += "$$ \\therefore M_{" + \
                      str(i + 1) + \
                      "}^{'} = {" + \
                      str(_InvM_[i]) + \
                      "} $$"
        value = 0
        result += "$$ \\begin{aligned} {x} &\equiv \sum_{i=1}^{" + \
                  str(self.length) + \
                  "} {{M}_{i}\cdot{M}_{i}^{'}\cdot{b}_{i}}\; mod \; {m} \\\\ &\equiv ("
        for i in range(self.length):
            result += "{" + \
                      str(_InvM_[i]) + \
                      "} \\times {" + \
                      str(_M_[i]) + \
                      "} \\times {" + \
                      str(self.remainder[i]) + \
                      "} "
            if i != self.length - 1:
                result += " + "
            value += _InvM_[i] * _M_[i] * self.remainder[i]
            value %= m
        result += ")\; mod \; {" + \
                  str(m) + \
                  "} \\\\ &\equiv {" + \
                  str(value) + \
                  "} \; mod \;{" + \
                  str(m) + \
                  "} \\\\ \\end{aligned} $$"
        return result

    def value(self):
        m = 1
        _M_ = []
        _InvM_ = []
        for i in range(self.length):
            m *= self.mod[i]
        for i in range(self.length):
            temp = 1
            for j in range(self.length):
                if self.mod[i] != self.mod[j]:
                    temp *= self.mod[j]
            _M_.append(temp)
        for i in range(self.length):
            temp = ExtendedEuclidean.ExtendedEuclidean(_M_[i], self.mod[i])
            _, x, _ = temp.value()
            _InvM_.append(x % self.mod[i])
        result = 0
        for i in range(self.length):
            result += _InvM_[i] * _M_[i] * self.remainder[i]
            result %= m

        return result, m


def judge_mod(mod):
    for i in range(len(mod)):
        for j in range(i + 1, len(mod)):
            x = ExtendedEuclidean.ExtendedEuclidean(mod[i], mod[j])
            r, _, _ = x.value()
            if r != 1:
                return False
    return True


def main():
    remainder = [1, 2, 4, 6]
    mod = [3, 5, 7, 13]
    x = CRT(remainder, mod)
    print(x.process())


if __name__ == '__main__':
    main()
