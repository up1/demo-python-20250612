"""
Format a range of numbers from a string input.
>>> format_range("[1,5]")
'1, 2, 3, 4, 5'
>>> format_range("[1,5)")
'1, 2, 3, 4'
>>> format_range("(1,5]")
'2, 3, 4, 5'
>>> format_range("(1,5)")
'2, 3, 4'
"""

def is_start_with_exclusive(input_string: str) -> bool:
    return input_string.startswith("[")

def is_end_with_exclusive(input_string: str) -> bool:
    return input_string.endswith("]")

def get_start_number(input_string: str) -> int:
    if is_start_with_exclusive(input_string):
        return int(input_string[1])
    else:
        return int(input_string[1])+ 1

def get_end_number(input_string: str) -> int:
    if is_end_with_exclusive(input_string):
        return int(input_string[-2])
    else:
        return int(input_string[-2]) - 1
    
def format_range(input_string: str) -> str:
    start = get_start_number(input_string)
    end = get_end_number(input_string)
    return ", ".join(str(i) for i in range(start, end + 1))

if __name__ == "__main__":
    import doctest
    doctest.testmod()