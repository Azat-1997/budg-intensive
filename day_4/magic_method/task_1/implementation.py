class Multiplier:
    
   def __init__(self, value) -> None:
        super().__init__()

   @classmethod
   def get_scale(cls):
       SCALES = {Hundred: 100, Thousand:1000, Million:1_000_000}
       return SCALES[cls]

   def __add__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
            result = self.get_value() + other.get_value()
        elif isinstance(other, (int, float)):
            result = self.get_value() + other
        else:
            raise TypeError
        
        cls = type(self)
        return cls(result / cls.get_scale())

   def __mul__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
            result = self.get_value() * other.get_value()
        elif isinstance(other, (int, float)):
            result = self.get_value() * other
        else:
            raise TypeError

        cls = type(self)
        return cls(result / cls.get_scale())


   def __sub__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
            result = self.get_value() - other.get_value()
        elif isinstance(other, (int, float)):
            result = self.get_value() - other
        else:
            raise TypeError
        cls = type(self)
        return cls(result / cls.get_scale())

   def __truediv__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
            result = self.get_value() / other.get_value()
        elif isinstance(other, (int, float)):
            result = self.get_value() / other
        else:
            raise TypeError
        cls = type(self)
        return cls(result / cls.get_scale())

class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        self.__value = value * Hundred.get_scale()

    def get_value(self):
        return self.__value 

class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        self.__value = value * Thousand.get_scale()

    def get_value(self):
        return self.__value

class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        self.__value = value * Million.get_scale()

    def get_value(self):
        return self.__value

