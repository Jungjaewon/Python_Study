"""

Python do not adopt "access modifier" such as public, protect, private like Java, C++.

In class, we use double under bar, single under bar variables for private and protect as the informal rule.

@property : get
@var_name.setter : setter

Ref : https://hamait.tistory.com/827
"""

class Test:

    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        print("Getter Called!! ", self._color)
        return self._color

    @color.setter
    def color(self,color):
        print("Setter Called!! ", color)
        self._color = color


class Celsius1:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    #temperature = property(get_temperature,set_temperature)
    # the property is inbuilt function.

class Celsius:
    def __init__(self):
        pass
    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

if __name__ == '__main__':
    """
    1. The first example

    t = Test("Red")
    t.color = "Blue" # setter
    t.__color = "Brown" # makes no error but does not work while using property
    t._color = "Brown" # makes no error but does work while using property
    print(t.color) # getter
    """
    t = Test("Red")
    t.color = "Blue"  # setter
    print(t.color)  # getter
    t._color = "Brown"  # makes no error but does not work while using property
    print(t.color)  # getter

    """
    2. The second example
    
    c = Celsius1()
    c._temperature = -300
    print(c.get_temperature())

    c = Celsius()
    #c.temperature = 100 # both are fine to set var.
    c._temperature = 100
    print(c.temperature)

    """

    """
    !!Caution!!
    double under bar var, func makes private access but these way are not recommended.
    double under bar var, func can not be called outside of the class scope.
    """




