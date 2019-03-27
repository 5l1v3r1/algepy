import math


class lineeq:
    """
    -------------------------
    Assuming y = 0
    y = mx + c
    Enter in order of m,c
    For linear equations
    -------------------------"""

    def __init__(self, m, c):
        """
        -----------------------------------
        self.yint for y intercept
        sefl.xint for x intercept
        self.gradient for gradient of line
        -----------------------------------"""
        self.m = m
        self.c = c
        self.gradient = m
        self.yint = c
        self.xint = m / -c


class quadeq:
    """
    -----------------------------------------------------------
    Assuming y = 0
    y = ax^2 + bx + c
    Enter in order of a, b, c
    If equation has no real solution, None will be returned for xint
    For quadratic equations
    -----------------------------------------------------------"""

    def __init__(self, a, b, c):
        """
        ----------------------------------------------
        self.xint for x intercept (if any)
        self.yint for y intercept
        self.tp for turning point (x,y)
        self.discrim for value of discriminant
        ----------------------------------------------"""
        self.a = a
        self.b = b
        self.c = c
        if (b ** 2 - 4 * a * c) < 0:
            self.xint = None
            self.yint = c
        else:
            discrim = (b ** 2 - 4 * a * c)
            coeff1 = (-b + math.sqrt(discrim)) / 2 * a
            coeff2 = (-b - math.sqrt(discrim)) / 2 * a
            temp = [coeff1, coeff2]
            tpx = (temp[0] + temp[1]) / 2
            tpy = (tpx ** 2 * a + b * tpx + c)
            tp = [tpx, tpy]
            self.tp = tp
            self.xint = temp
            self.discrim = discrim
            self.yint = c

    def subx(self, x):
        """returns value of y when x = (number) """
        value = (self.a * x) ** 2 + self.b * x + self.c
        return value


def gradient(x, cls):
    """Finds the gradient of a quadratic equation at a given point of x"""
    return cls.a * 2 * x + cls.b
