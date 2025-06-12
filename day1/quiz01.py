"""
Range Generator
>>> process("[1, 5]")
'1,2,3,4,5'
>>> process("(1, 5]")
'2,3,4,5'
>>> process("[1, 5)")
'1,2,3,4'
>>> process("(1, 5)")
'2,3,4'
"""

def process(input: str) -> str:
    start = get_start_number(input)
    end = get_end_number(input)
    result = ",".join(str(i) for i in range(start, end + 1))
    return result


def start_with_include(input) -> bool:
    return input[0] == "["

def end_with_include(input) -> bool:
    return input[-1] == "]"

def get_start_number(input)-> int:
    if start_with_include(input):
        return int(input[1])
    else:
        return int(input[1]) + 1

def get_end_number(input)-> int:
    if end_with_include(input):
        return int(input[-2])
    else:
        return int(input[-2]) - 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()