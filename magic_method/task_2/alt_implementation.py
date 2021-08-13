class MathClock:
    def __init__(self, hour=0, minute=0):
        self.__hour = hour 
        self.__minute = minute

    def get_hour(self):
        return self.__hour

    def set_hour(self, value):
         if isinstance(value, int) and 0 <= value < 24:
             self.__hour = value
         elif value < 0 or value >= 24:
             raise ValueError("Wrong format of hours")

         else:
             raise TypeError("Hours should to be integers")

    def get_minute(self):
        return self.__minute

    def set_minute(self, value):
        if isinstance(value, int) and 0 <= value < 60:
             self.__minute = value

        elif value < 0 or value >= 60:
             raise ValueError("Wrong format of minutes") 

        else:
             raise TypeError("Minutes should to be integers")

    def __str__(self):
        return "{0:02}:{1:02}".format(self.__hour, self.__minute)
       

    def get_time(self):
        return "{0:02}:{1:02}".format(self.__hour, self.__minute)

    def __add__(self, other):
        changed_minute = self.__minute + other
        if isinstance(other, int) and changed_minute < 60:
           return MathClock(self.__hour, changed_minute)
        elif changed_minute >= 60:
           raise ValueError("Too many minutes for adding")
        else:
           raise TypeError("Minutes should to be integers")

    def __mul__(self, other):
        changed_hour = self.__hour + other
        if isinstance(other, int) and changed_hour < 60:
           return MathClock(changed_hour, self.__minute)
        elif changed_hour >= 60:
           raise ValueError("Too many hours for adding")
        else:
           raise TypeError("Hours should to be integers")   

    def __sub__(self, other):
        changed_minute = self.__minute - other
        if isinstance(other, int) and changed_minute >= 0:
           return MathClock(self.__hour, changed_minute)
        elif changed_minute < 0:
           raise ValueError("Too many minutes to substract")
        else:
           raise TypeError("Minutes should to be integers")

    def __truediv__(self, other):
        changed_hour = self.__hour - other
        if isinstance(other, int) and changed_hour >= 0:
           return MathClock(changed_hour, self.__minute)
        elif changed_hour < 0:
           raise ValueError("Too many hours to substract")
        else:
           raise TypeError("Hours should to be integers")









