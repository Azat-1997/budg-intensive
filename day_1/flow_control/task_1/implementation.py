def get_numbers():
   
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    start = 1000
    end = 2000
    seq = []
    if end <= start:
        print("Warning: End should to be greater than start")
        
    for number in range(start, end):
        if number % 7 == 0 and number % 5 != 0:
            seq.append(number)
            
    return seq
