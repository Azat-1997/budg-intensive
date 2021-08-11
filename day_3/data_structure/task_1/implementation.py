class Tuple:
    """
    Создает неизменяемый объект, с упорядоченной структурой, методами count и index.
    При создание принимается последовательность объектов
    """
    def __init__(self, *args):
        self.args = args

    def __getitem__(self, key):
        return self.args[key]
    
    def __repr__(self):
        return str(self.args)
    
    def count(self, value):
        """
        Возвращает число раз появления value в объекте
        Args:
            value: Элемент число вхождения которого ищется в объекте
        """
        counter = 0
        for element in self.args:
            if element == value:
                counter += 1

        return counter

    def index(self, value):
        """
        Возвращает индекс первого вхождения элемента в объекте
        Args:
            value: Элемент индекс которого ищется в объекте
        """

        # Вернем -1 если вхождений нет
        for number, element in enumerate(self.args):
            if element == value:
                res = number
                break
        else:
            raise ValueError

        return res
