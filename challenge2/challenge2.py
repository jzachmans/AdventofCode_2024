def parse():
    p_list = []
    with open("challenge2.input", "r") as file:
        data = file.readlines()
    for line in data:
        p_list.append(tuple(line.strip("\n").split(" ")))
    return p_list


def challenge2_part1(p_list):
    unsafe_list = 0
    safe_list = 0
    for line in p_list:
        diffs = []
        count = 0
        while count < len(line) - 1:
            x = int(line[count])
            y = int(line[count + 1])
            # two consecutive readings, line is unsafe
            if x == y:
                unsafe_list += 1
                break
            # outside of range, line is unsafe
            if x - y not in range(-3, 4):
                pass
                unsafe_list += 1
                break
            # if we made it this far, we need to check that the whole line is  negative or positive
            diffs.append(x - y)
            count += 1
        # done processing readings on line, can continue
        if count == len(line) - 1:
            # check if all readings are either positive or negative
            all_positive = all(x > 0 for x in diffs)
            all_negative = all(x < 0 for x in diffs)
            if all_positive or all_negative:
                safe_list += 1
            else:
                unsafe_list += 1
    return safe_list


if __name__ == "__main__":
    p_list = parse()
    print(f"The challenge2/part1 answer is: {challenge2_part1(p_list)}")
    # print(f"The challenge1/part2 answer is: {challenge1_part2(left_list, right_list)}")
