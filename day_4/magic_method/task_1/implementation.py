class Multiplier:
    
   def __init__(self, value) -> None:
        super().__init__()

   @classmethod
   def get_scale(cls):
       scaling_factor = None
       if cls == Hundred:
            scaling_factor = 100
       elif cls == Thousand:
            scaling_factor = 1000
       elif cls == Million:
            scaling_factor = 1_000_000        
       return scaling_factor

   def __add__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
            result = self.get_value() + other.get_value()
        elif isinstance(other, (int, float)):
            result = self.get_value() + other
        else:
            raise TypeError
        return result 

   def __mul__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
            result = self.get_value() * other.get_value()
        elif isinstance(other, (int, float)):
            result = self.get_value() * other
        else:
            raise TypeError
        return result 

   def __sub__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
            result = self.get_value() - other.get_value()
        elif isinstance(other, (int, float)):
            result = self.get_value() - other
        else:
            raise TypeError
        return result

   def __truediv__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
            result = self.get_value() / other.get_value()
        elif isinstance(other, (int, float)):
            result = self.get_value() / other
        else:
            raise TypeError
        return result

class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        self.__value = value * Hundred.get_scale() 

    def get_value(self):
        return self.__value 

    def __add__(self, other):
        return Hundred(super().__add__(other) / Hundred.get_scale())

    def __mul__(self, other):
        return Hundred(super().__mul__(other) / Hundred.get_scale())
    
    def __sub__(self, other):
        return Hundred(super().__sub__(other) / Hundred.get_scale())

    def __truediv__(self, other):
        return Hundred(super().__truediv__(other) / Hundred.get_scale())

class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        self.__value = value * Thousand.get_scale()

    def get_value(self):
        return self.__value
    def __add__(self, other):
        return Thousand(super().__add__(other) / Thousand.get_scale())

    def __mul__(self, other):
        return Thousand(super().__mul__(other) / Thousand.get_scale())

    def __sub__(self, other):
        return Thousand(super().__sub__(other) / Thousand.get_scale())

    def __truediv__(self, other):
        return Thousand(super().__truediv__(other) / Thousand.get_scale())

class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        self.__value = value * Million.get_scale()

    def get_value(self):
        return self.__value

    def __add__(self, other):
        return Million(super().__add__(other) / Million.get_scale())

    def __mul__(self, other):
        return Million(super().__mul__(other) / Million.get_scale())

    def __sub__(self, other):
        return Million(super().__sub__(other) / Million.get_scale())

    def __truediv__(self, other):
        return Million(super().__truediv__(other) / Million.get_scale())
