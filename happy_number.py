def happy_number(n):
    if n == 1:
        return True

    number_str = str(n)

    if happy_number_aux(number_str,0) == 1:
        return True

    return False


def happy_number_aux(number_str, count_loops):
    new_number = 0

    count_loops += 1
    if count_loops > 100:
        return new_number

    for i in range(len(number_str)):
        new_number += int(number_str[i]) * int(number_str[i])

    if new_number == 1:
        return new_number
    else:
        return happy_number_aux(str(new_number), count_loops)


if __name__ == "__main__":
    print(happy_number(19))
    print(happy_number(2))
    print(happy_number(7))
    print(happy_number(1111111))
