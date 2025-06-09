def sequence(n):
    if n <= 1:
        return n

    return sequence(n - 1) + sequence(n - 2)

def locate(num, seq):
    if num in seq:
        return f'The number - {num} is at index {seq.index(num)}'
    else:
        return f"The number {num} is not in the sequence"