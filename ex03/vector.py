class Vector:

    def __init__(self, value=[], size=0):

        self.value: list = []
        self.size: int = 0
        if size and not value:
            dvalue = 0.0
            for i in range(0, size):
                self.value.append(dvalue)
            self.size = size

        elif value and (isinstance(value, list) or isinstance(value, range)):
            for val in value:
                self.value.append(float(val))
            self.size = len(self.value)

        elif value and isinstance(value, tuple):
            rvalue = range(value[0], value[1])
            for val in rvalue:
                self.value.append(float(val))
            self.size = len(self.value)

    def __add__(self, other):
        # if type(other) == float:
        #    other = Vector.float_to_vector(other, self.size)
        return Vector.addition(self, other)

    def __radd__(self, other):
        # if type(other) == float:
        #    other = Vector.float_to_vector(other, self.size)
        return Vector.addition(other, self)

    def __sub__(self, other):
        # if type(other) == float:
        #   other = Vector.float_to_vector(other, self.size)
        return Vector.subtraction(self, other)

    def __rsub__(self, other):
        # if type(other) == float:
        #    other = Vector.float_to_vector(other, self.size)
        return Vector.subtraction(other, self)

    def __truediv__(self, other):
        other = Vector.float_to_vector(other, self.size)
        return Vector.division(self, other)

    def __rtruediv__(self, other):
        assert True, 'Division by vector impossible'

    def __mul__(self, other):
        if type(other) == float:
            other = Vector.float_to_vector(other, self.size)
        return Vector.multiplication(self, other)

    def __rmul__(self, other):
        if type(other) == float:
            other = Vector.float_to_vector(other, self.size)
        return Vector.multiplication(other, self)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        txt = "Value: {}, Size: {}"
        return txt.format(self.value, self.size)

    @staticmethod
    def float_to_vector(scalar, size):
        tmp = []
        for i in range(0, size):
            tmp.append(scalar)
        return Vector(tmp)

    @staticmethod
    def addition(v1, v2):
        assert isinstance(v2, Vector), 'ValueError: must be a vector type'
        assert v1.size == v2.size, 'SizeError: Size of vector must be the same'
        result = Vector()
        for i in range(0, v1.size):
            result.value.append(v1.value[i] + v2.value[i])
        return result

    @staticmethod
    def subtraction(v1, v2):
        assert isinstance(v2, Vector), 'ValueError: must be a vector type'
        assert v1.size == v2.size, 'SizeError: Size of vector must be the same'
        result = Vector()
        for i in range(0, v1.size):
            result.value.append(v1.value[i] - v2.value[i])
        return result

    @staticmethod
    def division(v1, v2):
        result = Vector()
        for i in range(0, v1.size):
            result.value.append(v1.value[i] / v2.value[i])
        return result

    @staticmethod
    def multiplication(v1, v2):
        assert v1.size == v2.size, 'SizeError: Size of vector must be the same'
        result = Vector()
        for i in range(0, v1.size):
            result.value.append(v1.value[i] * v2.value[i])
        return result
