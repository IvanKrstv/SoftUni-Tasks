file_name = input().split("\\")[-1]
name, extension = file_name.split(".")

print(f"File name: {name}\n"
      f"File extension: {extension}")