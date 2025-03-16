def is_valid(username: str) -> bool:
    # 1
    if len(username) < 3 or len(username) > 16:
        return False
    # 2
    for char in username:
        if not char.isalpha() and not char.isdigit() and char not in ("-", "_"):
            return False
    # 3
    if " " in username:
        return False

    return True

usernames = input().split(", ")
for name in usernames:
    if is_valid(name):
        print(name)