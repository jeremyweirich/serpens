class Askella0(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    def correct_instance_0(self, x):
        return self.constellation + x

    def correct_instance_1(self, x):
        return self.constellation + x

    def correct_instance_2(self, x):
        return self.constellation + x

    @classmethod
    def correct_cls_3(cls):
        return cls.radial_velocity

    @classmethod
    def correct_cls_4(cls):
        return cls.radial_velocity

    def instance_should_be_cls_5(self):
        return self.radial_velocity

    def instance_should_be_static_6(self, x):
        return x ** 10

    @classmethod
    def cls_should_be_static_7(self, x):
        return x ** 10


class Askella1(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @staticmethod
    def correct_static_0(x):
        return x ** 10

    @staticmethod
    def static_should_be_cls_1():
        return Askella1.radial_velocity

    def instance_should_be_static_2(self, x):
        return x ** 10

    def instance_should_be_static_3(self, x):
        return x ** 10

    def instance_should_be_static_4(self, x):
        return x ** 10

    @staticmethod
    def static_should_be_cls_5():
        return Askella1.radial_velocity

    @classmethod
    def cls_should_be_static_6(self, x):
        return x ** 10

    def instance_should_be_static_7(self, x):
        return x ** 10
