class Tuple:
    """
    Создает неизменяемый объект, с упорядоченной структурой, методами count и index.
    При создание принимается последовательность объектов
    """
    def __init__(self, *elements):
        self.elements = elements

    def __getitem__(self, key):
        return self.elements[key]
    
    def __str__(self):
        return str(self.elements)
    
    def count(self, value):
        """
        Возвращает число раз появления value в объекте
        Args:
            value: Элемент число вхождения которого ищется в объекте
        """
        counter = 0
        for element in self.elements:
            if element == value:
                counter += 1

        return counter

    def index(self, value):
        """
        Возвращает индекс первого вхождения элемента в объекте
        Args:
            value: Элемент индекс которого ищется в объекте
        """
        if value not in self.elements:
            raise ValueError
            
        for number, element in enumerate(self.elements):
            if element == value:
                return number
               
