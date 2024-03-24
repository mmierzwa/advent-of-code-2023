import sys

numbers: dict[str, str] = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
                           'seven': '7', 'eight': '8', 'nine': '9'}


def parse_calibration_value_from_line(line: str) -> int:
    first: str = get_first_number(line)
    second: str = get_second_number(line)
    result: str = first + second

    return int(result)


def get_first_number(line: str) -> str:
    for idx in range(len(line)):
        prefix: str = line[idx:]
        if len(prefix) < 1:
            continue

        if prefix[0].isdigit():
            return str(prefix[0])

        for number in numbers.items():
            if prefix.startswith(number[0]):
                return number[1]

    return ""


def get_second_number(line: str) -> str:
    for idx in range(len(line)):
        prefix: str = line[:-idx] if idx > 0 else line
        if len(prefix) < 1:
            continue

        if prefix[len(prefix)-1].isdigit():
            return str(prefix[len(prefix)-1])

        for number in numbers.items():
            if prefix.endswith(number[0]):
                return number[1]

    return ""


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) < 1:
        print("input file name required", file=sys.stderr)
        sys.exit(-1)

    input_filename = args[0]

    total = 0

    with open(input_filename, 'r') as input_file:
        for l in input_file:
            total += parse_calibration_value_from_line(l.rstrip())

    print(str(total))
