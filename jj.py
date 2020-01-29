class User(object):
    def sign_in(self):
        print("init complete")


def multiply_by2(item):
    return item * 2


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, arrows):
        self.name = NameError
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} arrows remaining')

    def run(self):
        print("run very fast! ")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg("borgie", 50, 100)

# print(hb1.run())
# print(hb1.attack())
# print(hb1.sign_in())

print(HybridBorg.mro())

# class A:
#     num = 10


# class B(A):
#     pass


# class C(A):
#     num = 1


# class D(B, C):
#     pass


# print(D.num)
# print(D.mro())
