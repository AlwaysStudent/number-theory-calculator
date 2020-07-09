"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
import random
import math
from pkg import interface
from pkg import PowerMod
from pkg import ExtendedEuclidean
from pkg import Jacobi


class PublicKey:
    def __init__(self):
        self.n = None
        self.e = None

    def set_n(self, n):
        self.n = n

    def set_e(self, e):
        self.e = e

    def check(self):
        if not (self.n and self.e):
            return False
        return True


class PrivateKey:
    def __init__(self):
        self.p = None
        self.q = None
        self.d = None
        self.public_key = None

    def set_p(self, p):
        self.p = p

    def set_q(self, q):
        self.q = q

    def set_d(self, d):
        self.d = d

    def set_public_key(self, public_key):
        if public_key.check:
            self.public_key = public_key
        else:
            self.public_key = None

    def check(self):
        if not (self.p and self.q and self.d and self.public_key):
            return False
        return True


class RSA(interface.Process, interface.Value, interface.Encode, interface.Decode):
    def __init__(self, bit_len, mode='SS'):
        self.public_key = PublicKey()
        self.private_key = PrivateKey()
        self.bit_len = bit_len
        self.mode = mode

    def process(self):
        result = "$$ \\begin{aligned} "
        prime_factory = GeneratePrimeFactory(self.bit_len, self.mode, 40)
        p = prime_factory.generate_prime()
        q = prime_factory.generate_prime()
        n = p * q
        phi_n = (p - 1) * (q - 1)
        result += "& random\;prime\;{p} = {" + str(p) + "} \\\\"
        result += "& random\;prime\;{q} = {" + str(q) + "} \\\\"
        result += "& {n} = {p} \\times {q} = {" + str(p) + "} \\times {" + str(q) + "} = {" + str(n) + "} \\\\"
        result += "& \\varphi({n}) = (p - 1)(q - 1) = ({" + str(p) + "} - 1)({" + str(q) + "} - 1) = {" + str(phi_n) + "} \\\\"
        while True:
            e = random.randrange(3, phi_n, 1)
            gcd_e_phi_n = math.gcd(phi_n, e)
            if gcd_e_phi_n != 1:
                continue
            else:
                break
        result += "& random\;select\;e\;from\;{3}\;to\; " + str(phi_n) + "\; which\; makes\; (e, \\varphi(n)) = 1 \\\\"
        result += "& e = {" + str(e) + "} \\\\"
        t = ExtendedEuclidean.ExtendedEuclidean(phi_n, e)
        _, _, d = t.value()
        if d < 0:
            d += phi_n
        self.public_key.set_n(n)
        self.public_key.set_e(e)
        self.private_key.set_public_key(self.public_key)
        self.private_key.set_d(d)
        self.private_key.set_p(p)
        self.private_key.set_q(q)
        result += "& calculate\; d\; which\; makes\; ed \\equiv {1} \;mod\;\\varphi(n) \\\\ \\end{aligned} $$"
        result += t.process()
        result += "$$ \\begin{aligned} & \\therefore d = " + str(d) + "\\\\"
        result += "& \\therefore PublicKey:(n, e) = (" + str(self.public_key.n) + ", " + str(self.public_key.e) + ") \\\\"
        result += "& \\therefore PrivateKey:(PublicKey(n, e), p, q, d) = ((" + str(self.private_key.public_key.n) + ", "
        result += str(self.private_key.public_key.e) + "), " + str(self.private_key.p) + ", " + str(self.private_key.q)
        result += ", " + str(self.private_key.d) + ") \\\\ \\end{aligned} $$"
        self.check()
        return result

    def value(self):
        prime_factory = GeneratePrimeFactory(self.bit_len, self.mode, 40)
        p = prime_factory.generate_prime()
        q = prime_factory.generate_prime()
        while p == q:
            p = prime_factory.generate_prime()
            q = prime_factory.generate_prime()
        n = p * q
        phi_n = (p - 1) * (q - 1)
        while True:
            e = random.randrange(3, phi_n, 1)
            gcd_e_phi_n = math.gcd(phi_n, e)
            if gcd_e_phi_n != 1:
                continue
            else:
                break
        _, _, d = ExtendedEuclidean.ExtendedEuclidean(phi_n, e).value()
        if d < 0:
            d += phi_n
        self.public_key.set_n(n)
        self.public_key.set_e(e)
        self.private_key.set_public_key(self.public_key)
        self.private_key.set_d(d)
        self.private_key.set_p(p)
        self.private_key.set_q(q)
        result = (self.private_key.public_key.n, self.private_key.public_key.e), self.private_key.p, self.private_key.q, self.private_key.d
        self.check()
        return result

    def check(self):
        try:
            assert self.public_key.n == self.private_key.p * self.private_key.q
            assert self.public_key.e * self.private_key.d % ((self.private_key.p - 1) * (self.private_key.q - 1)) == 1
            assert self.public_key.e < self.public_key.n
            assert self.private_key.d < self.public_key.n

        except AssertionError:
            raise ValueError("RSA init fail!")

    def encode(self, plain_text):
        self.check()
        plain_text_num = int(''.join([add_zero(bin(ord(i)).replace("0b", "")) for i in plain_text]), 2)
        t = PowerMod.PowerMod(plain_text_num, self.public_key.e, self.public_key.n)
        return t.value()

    def decode(self, crypto_text):
        self.check()
        t = PowerMod.PowerMod(crypto_text, self.private_key.d, self.private_key.public_key.n)
        qqq = t.value()
        plain_text_num_1 = bin(qqq).replace("0b", "")[::-1]
        temp = []
        if len(plain_text_num_1) % 8 == 0:
            length = len(plain_text_num_1) // 8
        else:
            length = len(plain_text_num_1) // 8 + 1
        for i in range(length):
            temp.append(plain_text_num_1[i * 8:i * 8 + 8])
        l = []
        for i in temp:
            l.append(chr(int(i[::-1], 2)))
        plain_text = "".join(l[::-1])
        return plain_text


class GeneratePrimeFactory:
    def __init__(self, bit_len, mode, times=0):
        self.bit_len = bit_len
        self.mode = mode
        self.times = times

    def primality_test(self, n):
        # test whether n is a prime number or not
        small_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
                            71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
                            151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                            233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                            317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
                            419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                            503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
                            607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                            701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
                            811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
                            911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013,
                            1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093,
                            1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193,
                            1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289,
                            1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399,
                            1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483,
                            1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571,
                            1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663,
                            1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759,
                            1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873,
                            1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987,
                            1993, 1997, 1999]
        for prime in small_prime_list:
            if n % prime == 0:
                return False
        return True

    def generate_prime(self):
        g = generate_rand_odd(self.bit_len)
        while not self.primality_test(g):
            if self.mode == "FM":
                g = generate_prime_by_fermat(self.bit_len, self.times)
            elif self.mode == "MR":
                g = generate_prime_by_MR(self.bit_len, self.times)
            elif self.mode == "SS":
                g = generate_prime_by_SS(self.bit_len, self.times)
        return g


def generate_rand_odd(bit_len):
    temp = 2 ** (bit_len - 1)
    odd = random.randrange(1, temp, 2)
    odd = odd + temp
    return odd


def is_congruent(a, b, n):
    r = (a-b) % n
    if r == 0:
        return True
    else:
        return False


"""用费尔马小定理对guessp进行一次测试
guessp是一个正整数
b也是一个正整数，范围是1到n-1
如果通过测试返回True
否则返回False"""


def one_fermat_test(guessp, b):
    guessp_1 = guessp-1
    result = pow(b, guessp_1, guessp)
    if result == 1:
        return True
    else:
        return False


"""用费尔马小定理对p进行多次测试，
p是一个是正整数
times是测试次数，一个正整数int，推荐30-100
如果通过了所有次的测试返回True
否则返回False"""


def many_fermat_test(p, times):
    for i in range(times):
        b = random.randrange(2, p, 1)
        if not one_fermat_test(p, b):
            return False
    return True


"""用费尔马测试方法生成指定长度的随机素数
bitlen是素数的长度
times是测试次数,是一个正整数，推荐30-100
返回一个找到的素数
"""


def generate_prime_by_fermat(bitlen, times):
    while True:
        guessp = generate_rand_odd(bitlen)
        if many_fermat_test(guessp, times):
            return guessp
        else:
            continue


"""将a分解为2的s次方乘以m的形式
a是一个正整数
返回一个tuple，两个元素是s和m
s是整数
m是正整数"""


def get_2power_mulm(a):
    if a == 0:
        return(0, 0)
    s = 0
    m = a
    while True:
        q, r = divmod(m, 2)
        if r == 0:
            s = s+1
            m = q
        else:
            return (s, m)


"""用MillerRabin方法对guessp进行一次测试
guessp是一个正整数
b也是一个正整数，范围是1到n-1
如果通过测试返回True
否则返回False"""


def one_MR_test(guessp, b):
    guessp_1 = guessp-1
    s, m = get_2power_mulm(guessp_1)
    r = 0
    z = pow(b, m, guessp)
    if z == 1:
        return True
    if z == guessp_1:
        return True
    while True:
        if r == s-1:
            return False
        r = r+1
        qqq, z = divmod(z*z, guessp)  # qqq没有用
        if z == guessp_1:
            return True


"""用MillerRabin方法对p进行多次测试，
p是一个正整数
times是测试次数，一个正整数，推荐30-100
如果通过了所有次的测试返回True
否则返回False"""


def many_MR_test(p, times):
    for i in range(times):
        b = random.randrange(2, p, 1)
        if not one_MR_test(p, b):
            return False
    return True


"""用MillerRabin方法生成指定长度的随机素数
bitlen是素数的bit长度
times是测试次数，一个正整数，推荐30-100
返回一个找到的素数
"""


def generate_prime_by_MR(bitlen, times):
    while True:
        guessp = generate_rand_odd(bitlen)
        if many_MR_test(guessp, times):
            return guessp
        else:
            continue


"""用SolovayStrassen方法对guessp进行一次测试
guessp是一个正整数
b也是一个正整数，范围是1到n-1
如果通过测试返回True
否则返回False"""


def one_SS_test(guessp, b):
    d, _, _ = ExtendedEuclidean.ExtendedEuclidean(guessp, b).value()
    if not d == 1:
        return False
    J = Jacobi.Jacobi(b, guessp).value()
    guessp_1 = guessp-1
    e, _ = divmod(guessp_1, 2)
    z = pow(b, e, guessp)
    if is_congruent(J, z, guessp):
        return True
    else:
        return False


"""用SolovayStrassen方法对p进行多次测试，
p是一个正整数
times是测试次数，一个正整数int，推荐30-100
如果通过了所有次的测试返回True
否则返回False"""


def many_SS_test(p, times):
    for i in range(times):
        b = random.randrange(2, p, 1)
        if not one_SS_test(p, b):
            return False
    return True


"""用SolovayStrassen方法生成指定长度的随机素数
bitlen是素数的bit长度
times是一个正整数int，推荐30-100
返回一个正整数是找到的素数
"""


def generate_prime_by_SS(bitlen, times):
    while True:
        guessp = generate_rand_odd(bitlen)
        if many_SS_test(guessp, times):
            return guessp
        else:
            continue


def add_zero(bin_text):
    return "0" * (8 - len(bin_text)) + bin_text


def main():
    r = RSA(20)
    print(r.process())
    x = r.encode("qwe")
    print(x)
    y = r.decode(x)
    print(y)


if __name__ == '__main__':
    main()
