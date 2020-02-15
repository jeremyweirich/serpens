class Dnoces0(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @classmethod
    def cls_should_be_static_0(self, x):
        return x ** 10

    def instance_should_be_cls_1(self):
        return self.radial_velocity

    @staticmethod
    def correct_static_2(x):
        return x ** 10

    @classmethod
    def correct_cls_3(cls):
        return cls.radial_velocity

    @staticmethod
    def static_should_be_cls_4():
        return Dnoces0.radial_velocity

    @staticmethod
    def static_should_be_cls_5():
        return Dnoces0.radial_velocity

    @classmethod
    def correct_cls_6(cls):
        return cls.radial_velocity

    @staticmethod
    def correct_static_7(x):
        return x ** 10


class Dnoces1(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @classmethod
    def correct_cls_0(cls):
        return cls.radial_velocity

    @staticmethod
    def correct_static_1(x):
        return x ** 10

    @staticmethod
    def static_should_be_cls_2():
        return Dnoces1.radial_velocity

    @classmethod
    def cls_should_be_static_3(self, x):
        return x ** 10

    def correct_instance_4(self, x):
        return self.constellation + x

    def correct_instance_5(self, x):
        return self.constellation + x

    def instance_should_be_static_6(self, x):
        return x ** 10

    def instance_should_be_static_7(self, x):
        return x ** 10
