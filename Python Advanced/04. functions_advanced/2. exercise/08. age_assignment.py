def age_assignment(*args, **kwargs):
    name_dict = {arg: 0 for arg in args}
    final_string = ''

    for letter, age in kwargs.items():
        for name in name_dict:
            if name.startswith(letter):
                name_dict[name] = age

    for name, age in sorted(name_dict.items()):
        final_string += f"{name} is {age} years old.\n"

    return final_string

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))