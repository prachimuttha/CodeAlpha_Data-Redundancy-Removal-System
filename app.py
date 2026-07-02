def remove_duplicates(input_file, output_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    unique_data = []

    for line in lines:
        line = line.strip()

        if line not in unique_data:
            unique_data.append(line)

    with open(output_file, "w") as file:
        for item in unique_data:
            file.write(item + "\n")

    print("Duplicate data removed successfully!")
    print("Clean file created!")

remove_duplicates("sample.txt", "cleaned_data.txt")