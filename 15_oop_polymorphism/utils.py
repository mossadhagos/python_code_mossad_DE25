from numbers import Number
 
def validet_numbers(value) -> None:
    for numbers in numbers:
        if not isinstance(numbers, Number):
            raise TypeError(f"elements must be numbers not {type(numbers)}")