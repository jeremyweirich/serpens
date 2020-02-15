class Asterion0(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @classmethod
    def cls_should_be_static_0(self, x):
        return x ** 10

    @staticmethod
    def correct_static_1(x):
        return x ** 10

    @classmethod
    def correct_cls_2(cls):
        return cls.radial_velocity

    @staticmethod
    def correct_static_3(x):
        return x ** 10

    @classmethod
    def cls_should_be_static_4(self, x):
        return x ** 10

    def correct_instance_5(self, x):
        return self.constellation + x

    @classmethod
    def correct_cls_6(cls):
        return cls.radial_velocity

    def instance_should_be_static_7(self, x):
        return x ** 10


class Asterion1(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @classmethod
    def cls_should_be_static_0(self, x):
        return x ** 10

    def instance_should_be_cls_1(self):
        return self.radial_velocity

    def instance_should_be_static_2(self, x):
        return x ** 10

    @staticmethod
    def static_should_be_cls_3():
        return Asterion1.radial_velocity

    @staticmethod
    def correct_static_4(x):
        return x ** 10

    @staticmethod
    def correct_static_5(x):
        return x ** 10

    @classmethod
    def correct_cls_6(cls):
        return cls.radial_velocity

    @staticmethod
    def static_should_be_cls_7():
        return Asterion1.radial_velocity
