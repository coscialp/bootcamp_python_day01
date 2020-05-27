from vector import Vector


class Matrix:

    def __init__(self, data: list = None, shape: tuple = None):
        self.data = []
        if not data and shape:
            for i in range(0, [], shape[0]):
                v = Vector(shape[1])
                self.data.append(v.value)




