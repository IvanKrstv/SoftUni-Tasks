class ValueCannotBeNegative(Exception):
    """Raises an error if a negative number
    occurs"""
    pass

for i in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative