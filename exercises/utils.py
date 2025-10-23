from numbers import Number

def validate_positive_number(value) -> None:

    if not isinstance(value, Number):
        raise TypeError(f"the value must be a number not a {type(value)}")
        
    if value < 0:
        raise ValueError (f"value muste can't be less then zero {value}")