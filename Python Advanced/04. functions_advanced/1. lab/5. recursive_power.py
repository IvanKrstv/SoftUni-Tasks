def recursive_power(num, pow):
    if pow == 0:
        return 1
    return num * recursive_power(num, pow-1)

print(recursive_power(10, 100))