def divide_players(skill: [int]) -> int:
    n = len(skill)
    total_power = 0
    num_by_quantity = dict()

    for number in skill:
        total_power += number
        if number not in num_by_quantity:
            num_by_quantity[number] = 0
        num_by_quantity[number] += 1

    target_power = total_power / (n / 2)
    if target_power - int(target_power) > 0:
        return -1
    target_power = int(target_power)

    index = 0
    quantity_group = 0
    return_array = 0

    while index < n:
        current_number = skill[index]
        current_target = abs(target_power - current_number)

        if current_target not in num_by_quantity or num_by_quantity[current_target] < 0:
            return -1

        if num_by_quantity[current_target] > 0 and num_by_quantity[current_number] > 0:
            num_by_quantity[current_target] -= 1
            num_by_quantity[current_number] -= 1
            quantity_group += 1
            return_array += current_number * current_target

        index += 1

    if quantity_group != (n // 2):
        return -1

    return return_array


if __name__ == '__main__':
    array_param = [3, 2, 5, 1, 3, 4]
    print(f"players: {array_param}")
    print(f"sum skill: {divide_players(array_param)}")
    array_param = [3, 4]
    print(f"players: {array_param}")
    print(f"sum skill: {divide_players(array_param)}")
    array_param = [1, 1, 2, 3]
    print(f"players: {array_param}")
    print(f"sum skill: {divide_players(array_param)}")
