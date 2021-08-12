class Multiplier:

    def __init__(self, value) -> None:
        super().__init__()


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        self.__value = value * 100

    def get_value(self):
        return self.__value 

    def __add__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Hundred((self.__value + other.get_value()) / 100) 
        elif isinstance(other, (int, float)):
           result = Hundred((self.__value + other) / 100)
        else:
           raise TypeError

        return result 

    def __sub__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Hundred((self.__value - other.get_value()) / 100)
        elif isinstance(other, (int, float)):
           result = Hundred((self.__value - other) / 100) 
        else:
           raise TypeError

        return result

    def __mul__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Hundred((self.__value * other.get_value()) / 100)
        elif isinstance(other, (int, float)):
           result = Hundred((self.__value * other) / 100)
        else:
           raise TypeError

        return result

    def __truediv__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Hundred((self.__value / other.get_value()) / 100)
        elif isinstance(other, (int, float)):
           result = Hundred((self.__value + other) / 100)
        else:
           raise TypeError

        return result



class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        self.__value = value * 1000

    def get_value(self):
        return self.__value

    def __add__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Thousand((self.__value + other.get_value()) / 1000)
        elif isinstance(other, (int, float)):
           result = Thousand((self.__value + other) / 1000)
        else:
           raise TypeError

        return result

    def __sub__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Thousand((self.__value - other.get_value()) / 1000)
        elif isinstance(other, (int, float)):
           result = Thousand((self.__value - other) / 1000)
        else:
           raise TypeError

        return result

    def __mul__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Thousand((self.__value * other.get_value()) / 1000)
        elif isinstance(other, (int, float)):
           result = Thousand((self.__value * other) / 1000)
        else:
           raise TypeError

        return result

    def __truediv__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Thousand((self.__value / other.get_value()) / 1000)
        elif isinstance(other, (int, float)):
           result = Thousand((self.__value + other) / 1000)
        else:
           raise TypeError

        return result

    

class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        self.__value = value * 1_000_000

    def get_value(self):
        return self.__value

    def __add__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Million((self.__value + other.get_value()) / 1_000_000)
        elif isinstance(other, (int, float)):
           result = Million((self.__value + other) / 1_000_000)
        else:
           raise TypeError

        return result

    def __sub__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Million((self.__value - other.get_value()) / 1_000_000)
        elif isinstance(other, (int, float)):
           result = Hundred((self.__value - other) / 1_000_000)
        else:
           raise TypeError

        return result

    def __mul__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Hundred((self.__value * other.get_value()) / 1_000_000)
        elif isinstance(other, (int, float)):
           result = Hundred((self.__value * other) / 1_000_000)
        else:
           raise TypeError

        return result

    def __truediv__(self, other):
        if isinstance(other, (Hundred, Thousand, Million)):
           result = Million((self.__value / other.get_value()) / 1_000_000)
        elif isinstance(other, (int, float)):
           result = Million((self.__value + other) / 1_000_000)
        else:
           raise TypeError

        return result

