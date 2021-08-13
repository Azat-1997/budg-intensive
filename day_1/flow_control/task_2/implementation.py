def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """
    result = value
    if to_scale == "F":
        result = (9/5) * value + 32
    elif to_scale == "C":
        result = (5/9) * (value - 32)


    return result
