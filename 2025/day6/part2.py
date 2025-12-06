f = open("./sample.txt")


def add_helper(add_list):
    res = 0
    for val in add_list:
        res += val

    return res


def multiply_helper(multi_list):
    res = 1
    for val in multi_list:
        res *= val

    return res


def solution():
    input = f.read()

    lines = input.strip().split("\n")
    # operator is always the last
    operator_line = lines[-1]
    data_lines = lines[: len(lines) - 1]
    max_len = max(len(line) for line in data_lines)

    positions = set()
    # each number with spaces is a column
    for col_idx in range(max_len):
        for row in data_lines:
            if row[col_idx] != " ":
                positions.add(col_idx)

    positions = list(positions)
    columns = []
    current_column = []

    # group positions seperated by spaces into columns
    for i, pos in enumerate(positions):
        if i == 0:
            current_column = [pos]
        else:
            prev_pos = positions[i - 1]

            has_gap = False
            for gap_pos in range(prev_pos + 1, pos):
                if [row[gap_pos] == " " for row in data_lines]:
                    has_gap = True
                    break

            if has_gap:
                columns.append(current_column)
                current_column = [pos]
            else:
                current_column.append(pos)

    if current_column:
        columns.append(current_column)

    res = 0

    # read each column from right to left and extract operators
    for col_idx in range(len(columns) - 1, -1, -1):
        col_positions = columns[col_idx]
        col_numbers = []

        # read each postion in column vertically
        for pos in col_positions:
            vertical_number = ""
            for row in data_lines:
                char = row[pos]
                if char != " ":
                    vertical_number += char

            if vertical_number:
                col_numbers.append(int(vertical_number))

        if operator_line:
            # gets the operator for column within columns range
            padded_op_line = operator_line.ljust(max_len)
            for pos in col_positions:
                if padded_op_line[pos] == "+":
                    res += add_helper(col_numbers)
                    continue
                elif padded_op_line[pos] == "*":
                    res += multiply_helper(col_numbers)
                    continue

    return res


r = solution()
print(r)
