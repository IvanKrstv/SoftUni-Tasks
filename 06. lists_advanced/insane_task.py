original_words = input().split()

while True:
    command = input().split()
    action = command[0]
    if action == "3:1":
        break

    if action == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        merged_elements = []
        if start_index not in range(len(original_words)):
            start_index = 0
        if end_index not in range(len(original_words)):
            end_index = len(original_words) - 1

        for index in range(start_index, end_index + 1):
            merged_elements.append(original_words[index])
        new_element = ["".join(merged_elements)]
        original_words = original_words[:start_index] + new_element + original_words[end_index + 1:]

    elif action == "divide":
        index = int(command[1])
        partitions = int(command[2])
        used_word = original_words[index]
        size_partition = len(used_word) // partitions
        split_word = []
        number_partition = 0
        for i in range(0, len(used_word), size_partition):
            number_partition += 1
            if number_partition == partitions:
                split_word.append(used_word[i:])
                break
            split_word.append(used_word[i:i + size_partition])
        original_words = original_words[:index] + split_word + original_words[index + 1:]

print(" ".join(original_words))