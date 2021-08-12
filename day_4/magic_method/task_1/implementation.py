class Multiplier:
    def __init__(self, value) -> None:
        super().__init__()

    def _evaluate(self, other, action):
        # генерируем подходящее выражение, чтобы далее вычислять значения в магических методах
        if isinstance(other, (Hundred, Thousand, Million)):
            result = eval(str(self.get_value()) + action + str(other.get_value()))
        elif isinstance(other, (int, float)):
            result = eval(str(self.get_value()) + action + str(other))
        else:
            raise TypeError
        
        return result

class Hundred(Multiplier):
    """Множитель на 100"""
    __SCALE = 100
    def __init__(self, value):
        self.__value = value * Hundred.__SCALE

    def get_value(self):
        return self.__value 

    def __add__(self, other):
        return Hundred(super()._evaluate(other, "+") / Hundred.__SCALE)
        
    def __sub__(self, other):
        return Hundred(super()._evaluate(other, "-") / Hundred.__SCALE)

    def __mul__(self, other):
        return Hundred(super()._evaluate(other, "*") / Hundred.__SCALE)

    def __truediv__(self, other):
        return Hundred(super()._evaluate(other, "/") / Hundred.__SCALE)


class Thousand(Multiplier):
    """Множитель на 1 000"""
    __SCALE = 1000
    def __init__(self, value):
        self.__value = value * Thousand.__SCALE

    def get_value(self):
        return self.__value

    def __add__(self, other):
        return Thousand(super()._evaluate(other, "+") / Thousand.__SCALE)

    def __sub__(self, other):
        return Thousand(super()._evaluate(other, "-") / Thousand.__SCALE)

    def __mul__(self, other):
        return Thousand(super()._evaluate(other, "*") / Thousand.__SCALE)

    def __truediv__(self, other):
        return Thousand(super()._evaluate(other, "/") / Thousand.__SCALE)

class Million(Multiplier):
    """Множитель на 1 000 000"""
    __SCALE = 1_000_000
    def __init__(self, value):
        self.__value = value * Million.__SCALE

    def get_value(self):
        return self.__value

    def __add__(self, other):
        return Million(super()._evaluate(other, "+") / Million.__SCALE)

    def __sub__(self, other):
        return Million(super()._evaluate(other, "-") / Million.__SCALE)

    def __mul__(self, other):
        return Million(super()._evaluate(other, "*") / Million.__SCALE)

    def __truediv__(self, other):
        return Million(super()._evaluate(other, "/") / Million.__SCALE)
