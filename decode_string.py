def decode_string(s):
    string_decoded = ""
    string_temp = ""
    index_anterior = 0
    for letter in s:
        if letter.isalpha():
            string_temp = string_temp + "" + letter
        elif letter.isdigit():
            if string_temp != "":
                string_decoded = string_decoded.join(string_temp * index_anterior)
                string_temp = ""

            index_anterior = int(letter)

    if string_temp != "":
        string_decoded = string_decoded + (string_temp * index_anterior)

    return string_decoded


if __name__ == '__main__':
    string_encoded = "3[a]2[bc]"
    print(decode_string(string_encoded))

    string_encoded = "3[a2[c]]"
    print(decode_string(string_encoded))
