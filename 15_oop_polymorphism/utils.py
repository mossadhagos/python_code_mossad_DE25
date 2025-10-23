from numbers import Number
 
def validet_numbers(value) -> None:
    if not isinstance(value, Number):
        raise TypeError(f"elements must be numbers not {type(value)}")