import re


def number_of_atoms(formula):
    letters_dictionary = dict()

    letters = re.findall(r'[A-Za-z]', formula)
    print(letters)
    for letter in letters:
        print(letter)

    numbers = re.findall(r'\d', formula)
    print(numbers)
    for number in numbers:
        print(number)

    for letter in formula:
        letters_dictionary[letter] = 1

    print(letters_dictionary)


if __name__ == '__main__':
    formula_param = "K4(ON(SO3)2)2"
    print(number_of_atoms(formula_param))

    formula = "Mg(OH)2"
    print(number_of_atoms(formula))
