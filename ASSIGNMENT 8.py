def count_lines(path):
    with open(path, "r") as f:
        return sum(1 for _ in f)


def extract_first_lines(path, n=2):
    lines = []

    with open(path, "r") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            lines.append(line)

    return lines


def write_lines(path, lines):
    with open(path, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output_first_two_lines.txt"

    # Count total lines
    total_lines = count_lines(input_file)

    # Extract first two lines
    first_two_lines = extract_first_lines(input_file, 2)

    # Write extracted lines to new file
    write_lines(output_file, first_two_lines)

    print("Total number of lines:", total_lines)
    print("First two lines extracted successfully.")
    print("Data written to:", output_file)