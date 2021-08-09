def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """

    month31 = {"декабрь", "январь", "март", "май", "июль", "август", "октябрь"}
    month30 = {"апрель", "июнь", "сентябрь", "ноябрь"}
    
    if month in month30:
        return 30
    elif month in month31:
        return 31
    elif month == "февраль":
        return 28
    else:
        return 0
        
