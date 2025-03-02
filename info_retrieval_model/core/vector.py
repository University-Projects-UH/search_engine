import math
import functools
EPS = 0.0000001

class Vector:
    def __init__(self, vector = {}, calc_norm = False):
        self.vector = vector
        if(calc_norm):
            self.calculate_norm()

    def values(self):
        return self.vector.values()

    def calculate_norm(self):
        self.norm = math.sqrt(functools.reduce(lambda a, b: a + (b * b), self.values(), 0))

    def __add__(self, other):
        if(type(other) is not Vector):
            raise TypeError("Wrong type, should be a Vector")
        new_vector = {}
        for term in self.vector:
            if(new_vector.__contains__(term) == False):
                new_vector[term] = self.vector[term]
            else:
                new_vector[term] += self.vector[term]

        for term in other:
            if(new_vector.__contains__(term) == False):
                new_vector[term] = other[term]
            else:
                new_vector[term] += other[term]
        return Vector(new_vector)

    def __mul__(self, other):
        new_vector = {}
        for term in self.vector:
            new_vector[term] = self.vector[term] * other

        return Vector(new_vector)

    def __truediv__(self, other):
        assert(other > EPS, "Error, division by zero")
        return self.__mul__(1 / other)

    def __sub__(self, other):
        if(type(other) is not Vector):
            raise TypeError("Wrong type, should be a Vector")
        return self.__add__(other * -1)


    def __iter__(self):
        return self.vector.__iter__()

    def __contains__(self, value):
        return self.vector.__contains__(value)

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, value):
        return self.vector[value]
