class RasElasedAustralis0(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    def correct_instance_0(self, x):
        return self.constellation + x

    @classmethod
    def cls_should_be_static_1(self, x):
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

    @classmethod
    def cls_should_be_static_5(self, x):
        return x ** 10

    @classmethod
    def cls_should_be_static_6(self, x):
        return x ** 10

    def instance_should_be_static_7(self, x):
        return x ** 10


class RasElasedAustralis1(object):
    radial_velocity = None

    def __init__(self, constellation):
        self.constellation = constellation

    @classmethod
    def correct_cls_0(cls):
        return cls.radial_velocity

    def correct_instance_1(self, x):
        return self.constellation + x

    def instance_should_be_static_2(self, x):
        return x ** 10

    def correct_instance_3(self, x):
        return self.constellation + x

    def correct_instance_4(self, x):
        return self.constellation + x

    def correct_instance_5(self, x):
        return self.constellation + x

    def instance_should_be_cls_6(self):
        return self.radial_velocity

    @classmethod
    def correct_cls_7(cls):
        return cls.radial_velocity
