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

    def instance_should_be_class(self):
        new_vel = self.radial_velocity + 1
        print(Armus.radial_velocity)
        print(Armus)
        return

    def instance_should_be_static(self, x):
        return x ** 10

    @staticmethod
    def static_should_be_class():
        return Armus.radial_velocity

    @classmethod
    def class_should_be_static(cls, x):
        return x ** 10

    def class_in_class(self):
        class Alrami:
            color = "red"

            def __init__(self):
                self.shape = "square"

            def get_color(self):
                return self.color

        return 5
