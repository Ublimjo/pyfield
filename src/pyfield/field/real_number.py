"""
Module to hold real number field
"""

from pyfield.field import Field


class RealNumber(Field):
    """
    Real number field

    >>> from pyfield import RealNumber
    >>> heigth = RealNumber('heigth')
    >>> heigth('1.85')
    >>> print(heigth.get)
    1.85
    """

    def __init__(self, name, **kwargs):
        super(RealNumber, self).__init__(name, **kwargs)

        self.name = name
        self.hold = 0.0

        self.transformator = [float] + kwargs.pop('transformator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            pass
