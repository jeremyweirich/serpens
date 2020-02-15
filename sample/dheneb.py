class Dheneb0(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @staticmethod
    def static_should_be_cls_0():
        return Dheneb0.radial_velocity

    @classmethod
    def correct_cls_1(cls):
        return cls.radial_velocity

    @classmethod
    def cls_should_be_static_2(self, x):
        return x ** 10

    @classmethod
    def correct_cls_3(cls):
        return cls.radial_velocity

    @classmethod
    def cls_should_be_static_4(self, x):
        return x ** 10

    def instance_should_be_cls_5(self):
        return self.radial_velocity

    @classmethod
    def correct_cls_6(cls):
        return cls.radial_velocity

    @staticmethod
    def correct_static_7(x):
        return x ** 10


class Dheneb1(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @classmethod
    def correct_cls_0(cls):
        return cls.radial_velocity

    @staticmethod
    def correct_static_1(x):
        return x ** 10

    def correct_instance_2(self, x):
        return self.constellation + x

    def instance_should_be_cls_3(self):
        return self.radial_velocity

    @staticmethod
    def correct_static_4(x):
        return x ** 10

    def instance_should_be_cls_5(self):
        return self.radial_velocity

    @staticmethod
    def static_should_be_cls_6():
        return Dheneb1.radial_velocity

    def instance_should_be_cls_7(self):
        return self.radial_velocity
