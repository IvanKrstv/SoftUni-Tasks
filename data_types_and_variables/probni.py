lines = int(input())

opened_bracket = False
count_closed_brackets = 0
count_left_brackets = 0
count_right_brackets = 0

for i in range(lines):
    char = input()
    if char == "(":
        opened_bracket = True
        count_left_brackets += 1
    elif char == ")":
        count_right_brackets += 1
        if opened_bracket:
            opened_bracket = False
            count_closed_brackets += 1

if count_left_brackets == count_right_brackets == count_closed_brackets:
    is_balanced = "BALANCED"
else:
    is_balanced = "UNBALANCED"

print(is_balanced)
