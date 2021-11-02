def get_denominator(file_name):
    try:
        with open(file_name) as file:
            number = file.read()
            if int(number) == 0:
                raise ValueError("'0' can not be used")
            return int(number)
    except IOError:
        print("No such file in working directory")
        exit()
    except ValueError:
        print(f"'{number}' is not an integer number")
        exit()


def get_list_of_numbers(denominator):
    new_list = []
    numbers = list(range(1, 101))
    for number in numbers:
        if number % denominator == 0:
            new_list.append(number)
    return new_list


def get_sum(list_of_numbers):
    return sum(list_of_numbers)


def write_result(number, name_of_result_file):
    with open(name_of_result_file, 'w') as file:
        file.write(str(number))


file_to_open = "number.txt"
number_of_denominator = get_denominator(file_to_open)
print(number_of_denominator)
numbers_list = get_list_of_numbers(number_of_denominator)
print(numbers_list)
number_to_write = get_sum(numbers_list)
print(number_to_write)
print(write_result(number_to_write, "number_to_write"))
