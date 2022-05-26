''' exercise complex numbers '''

import math

class ComplexNumber:
    def __init__(self, real, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return True if self.real == other.real and self.imaginary == other.imaginary else False
        elif self.imaginary == 0 and self.real == other:
            return True
        return False
    
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        self.real += other
        return self

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.imaginary * other.real + self.real * other.imaginary)
        self.real *= other
        self.imaginary *= other 
        return self
        
    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        self.real -= other
        return self

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            factor = other.real ** 2 + other.imaginary ** 2
            real = self.real * other.real + self.imaginary * other.imaginary
            imaginary = self.imaginary * other.real - self.real * other.imaginary
            return ComplexNumber(real / factor, imaginary / factor)
        return ComplexNumber(self.real / other, self.imaginary / other)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        constant = math.e ** self.real
        return ComplexNumber(constant * math.cos(self.imaginary) + constant * math.sin(self.imaginary))

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self * (-1) + other

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return ComplexNumber(other) / self
