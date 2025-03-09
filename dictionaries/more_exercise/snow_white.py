dwarfs = {}
dwarf_colors = {}

while True:
    data = input()
    if data == "Once upon a time":
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = data.split(" <:> ")
    dwarf_physics = int(dwarf_physics)

    dwarf_key = (dwarf_name, dwarf_hat_color)
    if dwarf_key not in dwarfs:
        dwarfs[dwarf_key] = 0
    if dwarfs[dwarf_key] < dwarf_physics:
        dwarfs[dwarf_key] = dwarf_physics

    if dwarf_hat_color not in dwarf_colors:
        dwarf_colors[dwarf_hat_color] = 0
    dwarf_colors[dwarf_hat_color] = len([dwarf for dwarf in dwarfs if dwarf[1] == dwarf_hat_color])

sorted_dict = {k:v for (k,v) in sorted(dwarfs.items(), key=lambda item: (-item[1], -dwarf_colors[item[0][1]]))}

for (name, color), physics in sorted_dict.items():
    print(f"({color}) {name} <-> {physics}")