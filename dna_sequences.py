# complexity O(N)
def find_repeated_dna_sequences(s: str):
    if len(s) < 10:
        return []

    lookup = {}
    current_substring = s[:10]  # first 10 chars
    lookup[current_substring] = 1

    for i in range(10, len(s)):
        letter = s[i]
        current_substring = current_substring[1:10] + letter

        if not current_substring in lookup:
            lookup[current_substring] = 0

        lookup[current_substring] += 1

    output = []
    for key in lookup.keys():
        if lookup[key] > 1:
            output.append(key)

    return output


if __name__ == '__main__':
    dna_sequence = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(find_repeated_dna_sequences(dna_sequence))

    dna_sequence = "AAAAAAAAAAAAA"
    print(find_repeated_dna_sequences(dna_sequence))