followers = {}

def new_follower(dic: dict, com):
    username = com[1]
    if username not in dic:
        dic[username] = [0, 0]
    return dic

def like(dic: dict, com):
    username, likes = com[1], int(com[2])
    if username not in dic:
        dic[username] = [likes, 0]
    else:
        dic[username][0] += likes

    return dic

def comment(dic: dict, com):
    username = com[1]
    if username not in dic:
        dic[username] = [0, 1]
    else:
        dic[username][1] += 1

    return dic

def blocked(dic: dict, com):
    username = com[1]
    if username not in dic:
        print(f"{username} doesn't exist.")
    else:
        del dic[username]

    return dic

while True:
    command = input().split(": ")
    action = command[0]
    if action == "Log out":
        break

    if action == "New follower":
        followers = new_follower(followers, command)
    elif action == "Like":
        followers = like(followers, command)
    elif action == "Comment":
        followers = comment(followers, command)
    elif action == "Blocked":
        followers = blocked(followers, command)

print(f"{len(followers.keys())} followers")
for follower in followers.keys():
    print(f"{follower}: {sum(followers[follower])}")