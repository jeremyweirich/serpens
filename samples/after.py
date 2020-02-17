class Armus:
    radial_velocity = 20

    def __init__(self, constellation):
        self.constellation = constellation

    @classmethod
    def correct_class(cls):
        return cls.radial_velocity

    @staticmethod
    def correct_static(x):
        return x ** 10

    def correct_instance(self, x):
        return self.constellation + x

    @classmethod
    def instance_should_be_class(cls):
        new_vel = cls.radial_velocity + 1
        print(cls.radial_velocity)
        print(cls)
        return

    @staticmethod
    def instance_should_be_static(x):
        return x ** 10

    @classmethod
    def static_should_be_class(cls):
        return cls.radial_velocity

    @staticmethod
    def class_should_be_static(x):
        return x ** 10

    def class_in_class(self):


        class Alrami:
            color = 'red'

            def __init__(self):
                self.shape = 'square'

            @classmethod
            def get_color(cls):
                return cls.color
        return 5
