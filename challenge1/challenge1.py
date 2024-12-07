def parse():
    left_list = []
    right_list = []
    with open("challenge1.input", "r") as file:
        data = file.readlines()
    for line in data:
        l = line.split("   ")
        left_list.append(int(l[0]))
        right_list.append(int(l[1]))
    return left_list, right_list


def challenge1_part1(left_list, right_list):
    sum_list = []
    count = 0
    left_list_s = sorted(left_list)
    right_list_s = sorted(right_list)
    while count < len(left_list):
        l = left_list_s[count]
        r = right_list_s[count]
        s = l - r
        # janky way to catch negative ints
        if s < 0:
            s = r - l
        sum_list.append(s)
        count += 1
    return sum(sum_list)


def challenge1_part2(left_list, right_list):
    sum_list = []
    count = 0
    for i in left_list:
        matches = [x for x in right_list if i == x]
        if len(matches) > 0:
            sum_list.append(i * len(matches))
    return sum(sum_list)


if __name__ == "__main__":
    left_list, right_list = parse()
    print(f"The challenge1/part1 answer is: {challenge1_part1(left_list, right_list)}")
    print(f"The challenge1/part2 answer is: {challenge1_part2(left_list, right_list)}")
