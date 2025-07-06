class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return Integer(int(float_value))

    @classmethod
    def from_roman(cls, value):
        pass