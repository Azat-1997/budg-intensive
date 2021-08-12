class MathClock:
    def __init__(self, hour=0, minute=0): 
        self.__hour = hour
        self.__minute = minute

    def get_time(self):

        return "{0:02}:{1:02}".format(self.__hour, self.__minute)

    def __add__(self, other):
        additional_hour, changed_minute = divmod(self.__minute + other,  60)
        if isinstance(other, int):
           self.__minute = changed_minute
           self.__hour += additional_hour
        else:
           raise TypeError("Minutes should to be integers")

    def __mul__(self, other):
        if isinstance(other, int):
           self.__hour = (self.__hour + other) % 24
        else:
           raise TypeError("Hours should to be integers")

    def __sub__(self, other):
        additional_hour, changed_minute = divmod(self.__minute - other, 60)
        if isinstance(other, int):
           self.__minute = changed_minute
           self.__hour = (self.__hour + additional_hour) % 24
        else:
           raise TypeError("Minutes should to be integers")

    def __truediv__(self, other):
        if isinstance(other, int):
           self.__hour = (self.__hour - other) % 24
        else:
           raise TypeError("Hours should to be integers")

