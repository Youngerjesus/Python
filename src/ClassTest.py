class MethodTypes:

    name = "Ragnar"

    def __init__(self, i):
        self.i = i

    def instanceMethod(self):
        self.name = "lothbrock"
        print(self.name)

    @classmethod
    def classMethod(cls):
        cls.name = "lagertha"
        print(cls.name)

    @staticmethod
    def staticMetohd():
        print("This is a static method")

m = MethodTypes(5)
m.instanceMethod()
m.classMethod()

MethodTypes.classMethod()
MethodTypes.staticMetohd()
