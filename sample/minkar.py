class Minkar0(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    def instance_should_be_cls_0(self):
        return self.radial_velocity

    def instance_should_be_static_1(self, x):
        return x ** 10

    def instance_should_be_cls_2(self):
        return self.radial_velocity

    @classmethod
    def correct_cls_3(cls):
        return cls.radial_velocity

    def correct_instance_4(self, x):
        return self.constellation + x

    @staticmethod
    def correct_static_5(x):
        return x ** 10

    @classmethod
    def cls_should_be_static_6(self, x):
        return x ** 10

    @staticmethod
    def correct_static_7(x):
        return x ** 10


class Minkar1(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    def correct_instance_0(self, x):
        return self.constellation + x

    @staticmethod
    def static_should_be_cls_1():
        return Minkar1.radial_velocity

    def correct_instance_2(self, x):
        return self.constellation + x

    @staticmethod
    def static_should_be_cls_3():
        return Minkar1.radial_velocity

    @staticmethod
    def static_should_be_cls_4():
        return Minkar1.radial_velocity

    @classmethod
    def cls_should_be_static_5(self, x):
        return x ** 10

    def instance_should_be_static_6(self, x):
        return x ** 10

    @classmethod
    def cls_should_be_static_7(self, x):
        return x ** 10
