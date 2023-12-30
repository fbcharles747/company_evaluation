def to_percentage(val:float)->str:
    """
    convert decimal number to percentage
    Args:
        val (float): The decimal number to convert
    Returns:
        str: percentage str of the data
    """
    return "{number:.2f} %".format(number=val*100)
