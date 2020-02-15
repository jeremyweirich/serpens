class AsellusPrimus0(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @classmethod
    def cls_should_be_static_0(self, x):
        return x ** 10

    @classmethod
    def correct_cls_1(cls):
        return cls.radial_velocity

    def correct_instance_2(self, x):
        return self.constellation + x

    @staticmethod
    def static_should_be_cls_3():
        return AsellusPrimus0.radial_velocity

    @classmethod
    def cls_should_be_static_4(self, x):
        return x ** 10

    def correct_instance_5(self, x):
        return self.constellation + x

    def correct_instance_6(self, x):
        return self.constellation + x

    def correct_instance_7(self, x):
        return self.constellation + x


class AsellusPrimus1(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @staticmethod
    def correct_static_0(x):
        return x ** 10

    def instance_should_be_static_1(self, x):
        return x ** 10

    def instance_should_be_cls_2(self):
        return self.radial_velocity

    def instance_should_be_cls_3(self):
        return self.radial_velocity

    @staticmethod
    def static_should_be_cls_4():
        return AsellusPrimus1.radial_velocity

    @classmethod
    def cls_should_be_static_5(self, x):
        return x ** 10

    def correct_instance_6(self, x):
        return self.constellation + x

    @classmethod
    def correct_cls_7(cls):
        return cls.radial_velocity
