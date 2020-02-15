class Murzim0(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @staticmethod
    def static_should_be_cls_0():
        return Murzim0.radial_velocity

    @classmethod
    def cls_should_be_static_1(self, x):
        return x ** 10

    @classmethod
    def cls_should_be_static_2(self, x):
        return x ** 10

    def correct_instance_3(self, x):
        return self.constellation + x

    def instance_should_be_static_4(self, x):
        return x ** 10

    def correct_instance_5(self, x):
        return self.constellation + x

    @staticmethod
    def correct_static_6(x):
        return x ** 10

    @classmethod
    def correct_cls_7(cls):
        return cls.radial_velocity


class Murzim1(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @classmethod
    def cls_should_be_static_0(self, x):
        return x ** 10

    def correct_instance_1(self, x):
        return self.constellation + x

    @staticmethod
    def static_should_be_cls_2():
        return Murzim1.radial_velocity

    @classmethod
    def cls_should_be_static_3(self, x):
        return x ** 10

    def instance_should_be_static_4(self, x):
        return x ** 10

    @classmethod
    def correct_cls_5(cls):
        return cls.radial_velocity

    def correct_instance_6(self, x):
        return self.constellation + x

    def instance_should_be_static_7(self, x):
        return x ** 10
