def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """

    month31 = {"декабрь", "январь", "март", "май", "июль", "август", "октябрь"}
    month30 = {"апрель", "июнь", "сентябрь", "ноябрь"}
    febrary = "февраль"
    result = 0
    if month in month30:
        result = 30
    elif month in month31:
        result = 31
    elif month == febrary:
        result = 28
    
    return result
        
