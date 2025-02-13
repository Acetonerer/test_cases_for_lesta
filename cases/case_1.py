

def is_even(value: int) -> bool:
    """
    Функция проверки четности числа путем анализа последнего бита числа
    :param value: int
    :return: bool
    """
    if not isinstance(value, int):
        return "value must be int!"
    return value & 1 == 0


print(is_even('true'))
