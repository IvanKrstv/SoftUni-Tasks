countries = input().split(", ")
capitals = input().split(", ")

my_dict = {country: city for (country, city) in zip(countries, capitals)}

for key, value in my_dict.items():
    print(f"{key} -> {value}")