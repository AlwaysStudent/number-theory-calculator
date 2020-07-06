"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
import random
import math
import Interface
import PowerMod
import ExtendedEuclidean
import Jacobi


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


class RSA(Interface.Process, Interface.Value, Interface.Encode, Interface.Decode):
    def __init__(self, bit_len, mode='FM'):
        self.public_key = PublicKey()
        self.private_key = PrivateKey()
        self.bit_len = bit_len
        self.mode = mode

    def process(self):
        result = "$$ \\begin{aligned} "
        prime_factory = GeneratePrimeFactory(self.bit_len, self.mode)
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
        return result

    def value(self):
        prime_factory = GeneratePrimeFactory(self.bit_len, self.mode)
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
        return (self.private_key.public_key.n, self.private_key.public_key.e), self.private_key.p, self.private_key.q, self.private_key.d

    def encode(self, plain_text):
        if len(plain_text) * 8 > self.bit_len - 11:
            raise ValueError("plain text is too long")
        plain_text_num = int(''.join([add_zero(bin(ord(i)).replace("0b", "")) for i in plain_text]), 2)
        t = PowerMod.PowerMod(plain_text_num, self.public_key.e, self.public_key.n)
        return t.value()

    def decode(self, crypto_text):
        t = PowerMod.PowerMod(crypto_text, self.private_key.d, self.private_key.public_key.n)

        

class GeneratePrimeFactory:
    def __init__(self, bit_len, mode):
        self.bit_len = bit_len
        self.mode = mode

    def generate_prime(self):
        g = None
        if self.mode == "FM":
            g = generate_prime_by_fermat(self.bit_len)
        elif self.mode == "MR":
            g = generate_prime_by_MR(self.bit_len)
        elif self.mode == "SS":
            g = generate_prime_by_SS(self.bit_len)
        return g


def generate_rand_odd(bit_len):
    temp = 2 ** (bit_len - 1)
    odd = random.randrange(1, temp, 2)
    odd = odd + temp
    return odd


def is_congruent(a, b, n):
    r = (a - b) % n
    if not r:
        return True
    else:
        return False


def one_fermat_test(guess_p, b):
    guess_p_1 = guess_p - 1
    result = PowerMod.PowerMod(b, guess_p_1, guess_p).value()
    if result:
        return True
    else:
        return False


def many_fermat_test(p, times):
    for _ in range(times):
        b = random.randrange(2, p, 1)
        if not one_fermat_test(p, b):
            return False
    return True


def generate_prime_by_fermat(bit_len, times=0):
    while True:
        guess_p = generate_rand_odd(bit_len)
        if not times:
            times = bit_len // 12
        if many_fermat_test(guess_p, times):
            return guess_p


def separate_prime_2(a):
    if a == 0:
        return 0, 0
    s = 0
    m = a
    while True:
        q, r = divmod(m, 2)
        if not r:
            s += 1
            m = q
        else:
            return s, m


def one_MR_test(guess_p, b):
    guess_p_1 = guess_p - 1
    s, m = separate_prime_2(guess_p_1)

    r = 0
    z = PowerMod.PowerMod(b, m, guess_p_1).value()
    if z:
        return True
    if z == guess_p_1:
        return True
    while True:
        if r == s - 1:
            return False
        r = r + 1
        _, z = divmod(z*z, guess_p)
        if z == guess_p_1:
            return True


def many_MR_test(p, times):
    for _ in range(times):
        b = random.randrange(2, p, 1)
        if not one_MR_test(p, b):
            return False
    return True


def generate_prime_by_MR(bit_len, times=0):
    while True:
        guess_p = generate_rand_odd(bit_len)
        if not times:
            times = bit_len // 12
        if many_MR_test(guess_p, times):
            return guess_p


def one_SS_test(guess_p, b):
    d = math.gcd(guess_p, b)
    if not d == 1:
        return False
    j = Jacobi.Jacobi(b, guess_p).value()
    guess_p_1 = guess_p - 1
    e, _ = divmod(guess_p_1, 2)  # rrr没有用
    z = PowerMod.PowerMod(b, e, guess_p).value()
    if is_congruent(j, z, guess_p):
        return True
    else:
        return False


def many_SS_test(p, times):
    for _ in range(times):
        b = separate_prime_2(p)
        if not one_SS_test(p, b):
            return False
    return True


def generate_prime_by_SS(bit_len, times=0):
    while True:
        guessp = generate_rand_odd(bit_len)
        if not times:
            times = bit_len // 12
        if many_SS_test(guessp, times):
            return guessp


def add_zero(bin_text):
    return "0" * (8 - len(bin_text)) + bin_text

def main():
    r = RSA(10)
    print(r.process())


if __name__ == '__main__':
    main()
