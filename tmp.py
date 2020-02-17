class Foo:
    bar = 10

    def instance_should_be_class(self):
        print(self.bar)

    def instance_should_be_static(self, x):
        return x ** 10

    @staticmethod
    def static_should_be_class():
        return Foo.bar

    @classmethod
    def class_should_be_static(cls, x):
        return x ** 10