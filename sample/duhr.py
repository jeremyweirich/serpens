class Duhr0(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @staticmethod
    def correct_static_0(x):
        return x ** 10

    def instance_should_be_cls_1(self):
        return self.radial_velocity

    @classmethod
    def correct_cls_2(cls):
        return cls.radial_velocity

    def instance_should_be_cls_3(self):
        return self.radial_velocity

    def correct_instance_4(self, x):
        return self.constellation + x

    @staticmethod
    def static_should_be_cls_5():
        return Duhr0.radial_velocity

    @classmethod
    def cls_should_be_static_6(self, x):
        return x ** 10

    @classmethod
    def cls_should_be_static_7(self, x):
        return x ** 10


class Duhr1(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    def instance_should_be_static_0(self, x):
        return x ** 10

    @classmethod
    def correct_cls_1(cls):
        return cls.radial_velocity

    @classmethod
    def cls_should_be_static_2(self, x):
        return x ** 10

    def correct_instance_3(self, x):
        return self.constellation + x

    @classmethod
    def cls_should_be_static_4(self, x):
        return x ** 10

    def instance_should_be_static_5(self, x):
        return x ** 10

    @staticmethod
    def correct_static_6(x):
        return x ** 10

    @classmethod
    def correct_cls_7(cls):
        return cls.radial_velocity
